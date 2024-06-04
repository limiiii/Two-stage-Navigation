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

class get_photoRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type get_photoRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type get_photoRequest
    let len;
    let data = new get_photoRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/get_photoRequest';
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
    const resolved = new get_photoRequest(null);
    return resolved;
    }
};

class get_photoResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.is_done = null;
    }
    else {
      if (initObj.hasOwnProperty('is_done')) {
        this.is_done = initObj.is_done
      }
      else {
        this.is_done = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type get_photoResponse
    // Serialize message field [is_done]
    bufferOffset = _serializer.bool(obj.is_done, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type get_photoResponse
    let len;
    let data = new get_photoResponse(null);
    // Deserialize message field [is_done]
    data.is_done = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'fusion/get_photoResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ccf1bf44aca57c0fac7595ea9e4b924c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool is_done
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new get_photoResponse(null);
    if (msg.is_done !== undefined) {
      resolved.is_done = msg.is_done;
    }
    else {
      resolved.is_done = false
    }

    return resolved;
    }
};

module.exports = {
  Request: get_photoRequest,
  Response: get_photoResponse,
  md5sum() { return 'ccf1bf44aca57c0fac7595ea9e4b924c'; },
  datatype() { return 'fusion/get_photo'; }
};
