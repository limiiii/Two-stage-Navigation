// Auto-generated. Do not edit!

// (in-package fusion.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class yolo_modelRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yolo_modelRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yolo_modelRequest
    let len;
    let data = new yolo_modelRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/yolo_modelRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yolo_modelRequest(null);
    return resolved;
    }
};

class yolo_modelResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Class = null;
      this.xmid = null;
      this.ymid = null;
    }
    else {
      if (initObj.hasOwnProperty('Class')) {
        this.Class = initObj.Class
      }
      else {
        this.Class = [];
      }
      if (initObj.hasOwnProperty('xmid')) {
        this.xmid = initObj.xmid
      }
      else {
        this.xmid = [];
      }
      if (initObj.hasOwnProperty('ymid')) {
        this.ymid = initObj.ymid
      }
      else {
        this.ymid = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yolo_modelResponse
    // Serialize message field [Class]
    bufferOffset = _arraySerializer.string(obj.Class, buffer, bufferOffset, null);
    // Serialize message field [xmid]
    bufferOffset = _arraySerializer.int64(obj.xmid, buffer, bufferOffset, null);
    // Serialize message field [ymid]
    bufferOffset = _arraySerializer.int64(obj.ymid, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yolo_modelResponse
    let len;
    let data = new yolo_modelResponse(null);
    // Deserialize message field [Class]
    data.Class = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [xmid]
    data.xmid = _arrayDeserializer.int64(buffer, bufferOffset, null)
    // Deserialize message field [ymid]
    data.ymid = _arrayDeserializer.int64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.Class.forEach((val) => {
      length += 4 + _getByteLength(val);
    });
    length += 8 * object.xmid.length;
    length += 8 * object.ymid.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/yolo_modelResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '413fba5d33e359512198fd983aafb45c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] Class
    int64[] xmid
    int64[] ymid
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yolo_modelResponse(null);
    if (msg.Class !== undefined) {
      resolved.Class = msg.Class;
    }
    else {
      resolved.Class = []
    }

    if (msg.xmid !== undefined) {
      resolved.xmid = msg.xmid;
    }
    else {
      resolved.xmid = []
    }

    if (msg.ymid !== undefined) {
      resolved.ymid = msg.ymid;
    }
    else {
      resolved.ymid = []
    }

    return resolved;
    }
};

module.exports = {
  Request: yolo_modelRequest,
  Response: yolo_modelResponse,
  md5sum() { return '413fba5d33e359512198fd983aafb45c'; },
  datatype() { return 'fusion/yolo_model'; }
};
