# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T01:37:29.044722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `-0.226` n `228`; crypto_major avg `-0.2275` n `8`; equity avg `-0.0726` n `74`; fx avg `0.0283` n `6`; index avg `-0.0321` n `23`; metal avg `0.0469` n `18`; unknown avg `-0.0893` n `547`
- 1h: commodity avg `-0.4395` n `12`; crypto_alt avg `0.0888` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `0.0457` n `74`; fx avg `0.0313` n `6`; index avg `0.0828` n `23`; metal avg `0.143` n `18`; unknown avg `-0.0623` n `547`
- 4h: commodity avg `-0.1098` n `12`; crypto_alt avg `-0.3008` n `228`; crypto_major avg `-0.7435` n `8`; equity avg `0.0531` n `74`; fx avg `0.0177` n `6`; index avg `0.087` n `23`; metal avg `-0.917` n `18`; unknown avg `-0.4598` n `547`
- 24h: commodity avg `-0.6124` n `12`; crypto_alt avg `-0.2233` n `228`; crypto_major avg `-2.307` n `8`; equity avg `-1.8778` n `74`; fx avg `0.0836` n `6`; index avg `-0.8418` n `23`; metal avg `-2.3547` n `18`; unknown avg `-0.4768` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0368`, n `668`, weak_sample_signal
