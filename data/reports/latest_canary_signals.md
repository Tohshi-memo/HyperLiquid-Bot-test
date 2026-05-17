# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T17:37:19.671814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.2` n `228`; crypto_major avg `-0.0462` n `8`; equity avg `0.0031` n `65`; fx avg `0.0` n `5`; index avg `0.0132` n `23`; metal avg `0.012` n `18`; unknown avg `0.0714` n `384`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.7529` n `228`; crypto_major avg `-0.3935` n `8`; equity avg `-0.1188` n `65`; fx avg `0.0116` n `5`; index avg `-0.0863` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.0977` n `384`
- 4h: commodity avg `-0.0692` n `12`; crypto_alt avg `-0.7502` n `228`; crypto_major avg `-0.3728` n `8`; equity avg `-0.089` n `65`; fx avg `0.0322` n `5`; index avg `0.0531` n `23`; metal avg `0.0182` n `18`; unknown avg `0.0133` n `383`
- 24h: commodity avg `1.7446` n `12`; crypto_alt avg `-9.8158` n `228`; crypto_major avg `-2.7435` n `8`; equity avg `-2.6484` n `65`; fx avg `-0.1543` n `5`; index avg `-1.622` n `23`; metal avg `-5.8449` n `18`; unknown avg `550.0175` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
