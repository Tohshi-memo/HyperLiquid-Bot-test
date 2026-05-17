# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T15:37:17.419953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `0.0415` n `228`; crypto_major avg `-0.0424` n `8`; equity avg `0.0067` n `65`; fx avg `0.0` n `5`; index avg `0.0209` n `23`; metal avg `0.0044` n `18`; unknown avg `-0.0181` n `384`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `0.1542` n `228`; crypto_major avg `0.1474` n `8`; equity avg `0.016` n `65`; fx avg `-0.0009` n `5`; index avg `0.0536` n `23`; metal avg `0.0341` n `18`; unknown avg `-0.0374` n `383`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.3258` n `228`; crypto_major avg `-0.2485` n `8`; equity avg `0.0065` n `65`; fx avg `0.0013` n `5`; index avg `0.0707` n `23`; metal avg `0.0321` n `18`; unknown avg `-0.0474` n `383`
- 24h: commodity avg `1.7367` n `12`; crypto_alt avg `-9.2739` n `228`; crypto_major avg `-2.4958` n `8`; equity avg `-2.6016` n `65`; fx avg `-0.1657` n `5`; index avg `-1.5968` n `23`; metal avg `-5.8307` n `18`; unknown avg `550.0078` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
