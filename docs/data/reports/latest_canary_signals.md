# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T12:22:14.478419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `-0.0168` n `228`; crypto_major avg `0.0977` n `8`; equity avg `-0.0581` n `65`; fx avg `0.0017` n `5`; index avg `-0.061` n `23`; metal avg `-0.007` n `18`; unknown avg `0.0531` n `383`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.0204` n `228`; crypto_major avg `0.0922` n `8`; equity avg `-0.0248` n `65`; fx avg `-0.0177` n `5`; index avg `-0.0491` n `23`; metal avg `0.0049` n `18`; unknown avg `-0.0178` n `383`
- 4h: commodity avg `0.047` n `12`; crypto_alt avg `-0.0573` n `228`; crypto_major avg `0.4815` n `8`; equity avg `0.2543` n `65`; fx avg `-0.013` n `5`; index avg `0.0891` n `23`; metal avg `-0.0554` n `18`; unknown avg `0.0019` n `383`
- 24h: commodity avg `1.7686` n `12`; crypto_alt avg `-8.9973` n `228`; crypto_major avg `-2.1979` n `8`; equity avg `-2.6619` n `65`; fx avg `-0.1844` n `5`; index avg `-1.7131` n `23`; metal avg `-5.8557` n `18`; unknown avg `550.1096` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
