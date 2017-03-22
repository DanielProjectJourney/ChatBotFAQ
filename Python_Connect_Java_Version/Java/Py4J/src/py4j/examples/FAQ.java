/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package py4j.examples;

/**
 *
 * @author daniel
 */
public interface FAQ {
    
    public void setQuestion(String question);

    public String getQuestion();

    public void setAnswer(String answer);
    
    public String getAnswer();
    
    //Save the Question & Answer into Pickle File (Serializable)
    public void serialize();
}
