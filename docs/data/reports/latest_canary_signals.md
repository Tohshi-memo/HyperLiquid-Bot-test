# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T17:41:21.399117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1525` n `228`; crypto_major avg `0.0563` n `8`; equity avg `-0.0158` n `65`; fx avg `0.0` n `5`; index avg `0.0114` n `23`; metal avg `0.022` n `18`; unknown avg `0.0838` n `384`
- 1h: commodity avg `-0.0305` n `12`; crypto_alt avg `-0.7059` n `228`; crypto_major avg `-0.2915` n `8`; equity avg `-0.1376` n `65`; fx avg `0.0116` n `5`; index avg `-0.0881` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.0961` n `384`
- 4h: commodity avg `-0.0591` n `12`; crypto_alt avg `-0.7034` n `228`; crypto_major avg `-0.2697` n `8`; equity avg `-0.1078` n `65`; fx avg `0.0322` n `5`; index avg `0.0514` n `23`; metal avg `0.0283` n `18`; unknown avg `-0.0138` n `383`
- 24h: commodity avg `1.755` n `12`; crypto_alt avg `-9.7748` n `228`; crypto_major avg `-2.6403` n `8`; equity avg `-2.6678` n `65`; fx avg `-0.1543` n `5`; index avg `-1.6238` n `23`; metal avg `-5.836` n `18`; unknown avg `549.962` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
