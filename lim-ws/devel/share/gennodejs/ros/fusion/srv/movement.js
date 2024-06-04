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

class movementRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.xmax = null;
      this.xmin = null;
      this.ymin = null;
      this.ymax = null;
    }
    else {
      if (initObj.hasOwnProperty('xmax')) {
        this.xmax = initObj.xmax
      }
      else {
        this.xmax = 0;
      }
      if (initObj.hasOwnProperty('xmin')) {
        this.xmin = initObj.xmin
      }
      else {
        this.xmin = 0;
      }
      if (initObj.hasOwnProperty('ymin')) {
        this.ymin = initObj.ymin
      }
      else {
        this.ymin = 0;
      }
      if (initObj.hasOwnProperty('ymax')) {
        this.ymax = initObj.ymax
      }
      else {
        this.ymax = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type movementRequest
    // Serialize message field [xmax]
    bufferOffset = _serializer.int64(obj.xmax, buffer, bufferOffset);
    // Serialize message field [xmin]
    bufferOffset = _serializer.int64(obj.xmin, buffer, bufferOffset);
    // Serialize message field [ymin]
    bufferOffset = _serializer.int64(obj.ymin, buffer, bufferOffset);
    // Serialize message field [ymax]
    bufferOffset = _serializer.int64(obj.ymax, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type movementRequest
    let len;
    let data = new movementRequest(null);
    // Deserialize message field [xmax]
    data.xmax = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [xmin]
    data.xmin = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [ymin]
    data.ymin = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [ymax]
    data.ymax = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/movementRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '05b4d605c3540d174c215ee6e529e83d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 xmax
    int64 xmin
    int64 ymin
    int64 ymax
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new movementRequest(null);
    if (msg.xmax !== undefined) {
      resolved.xmax = msg.xmax;
    }
    else {
      resolved.xmax = 0
    }

    if (msg.xmin !== undefined) {
      resolved.xmin = msg.xmin;
    }
    else {
      resolved.xmin = 0
    }

    if (msg.ymin !== undefined) {
      resolved.ymin = msg.ymin;
    }
    else {
      resolved.ymin = 0
    }

    if (msg.ymax !== undefined) {
      resolved.ymax = msg.ymax;
    }
    else {
      resolved.ymax = 0
    }

    return resolved;
    }
};

class movementResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.radian = null;
      this.distance = null;
    }
    else {
      if (initObj.hasOwnProperty('radian')) {
        this.radian = initObj.radian
      }
      else {
        this.radian = 0.0;
      }
      if (initObj.hasOwnProperty('distance')) {
        this.distance = initObj.distance
      }
      else {
        this.distance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type movementResponse
    // Serialize message field [radian]
    bufferOffset = _serializer.float64(obj.radian, buffer, bufferOffset);
    // Serialize message field [distance]
    bufferOffset = _serializer.float64(obj.distance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type movementResponse
    let len;
    let data = new movementResponse(null);
    // Deserialize message field [radian]
    data.radian = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distance]
    data.distance = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/movementResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd752a56f82b7255790c9bb8872aed2f4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 radian
    float64 distance
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new movementResponse(null);
    if (msg.radian !== undefined) {
      resolved.radian = msg.radian;
    }
    else {
      resolved.radian = 0.0
    }

    if (msg.distance !== undefined) {
      resolved.distance = msg.distance;
    }
    else {
      resolved.distance = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: movementRequest,
  Response: movementResponse,
  md5sum() { return 'f700a31e1923a44559cb0687bf6c8500'; },
  datatype() { return 'fusion/movement'; }
};
