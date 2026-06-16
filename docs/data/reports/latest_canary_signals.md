# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T05:22:26.969120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `0.0874` n `228`; crypto_major avg `0.1297` n `8`; equity avg `0.0709` n `77`; fx avg `0.0019` n `6`; index avg `-0.3527` n `23`; metal avg `-0.0128` n `18`; unknown avg `0.1933` n `687`
- 1h: commodity avg `-0.1038` n `12`; crypto_alt avg `0.1346` n `228`; crypto_major avg `0.3551` n `8`; equity avg `0.0847` n `77`; fx avg `-0.0255` n `6`; index avg `-0.207` n `23`; metal avg `0.044` n `18`; unknown avg `-0.2082` n `687`
- 4h: commodity avg `-0.3239` n `12`; crypto_alt avg `-0.2074` n `228`; crypto_major avg `0.215` n `8`; equity avg `0.4792` n `77`; fx avg `-0.0149` n `6`; index avg `-0.1132` n `23`; metal avg `0.2241` n `18`; unknown avg `-0.0878` n `679`
- 24h: commodity avg `0.1832` n `12`; crypto_alt avg `0.2146` n `228`; crypto_major avg `2.1457` n `8`; equity avg `1.1866` n `76`; fx avg `-0.1018` n `6`; index avg `0.2805` n `23`; metal avg `-0.3711` n `18`; unknown avg `0.9845` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
