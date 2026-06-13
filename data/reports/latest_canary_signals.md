# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T16:37:30.934108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0976` n `12`; crypto_alt avg `-0.1529` n `228`; crypto_major avg `-0.1324` n `8`; equity avg `-0.0566` n `74`; fx avg `0.0` n `6`; index avg `0.0128` n `23`; metal avg `0.1733` n `18`; unknown avg `0.0101` n `644`
- 1h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.5798` n `228`; crypto_major avg `-0.6041` n `8`; equity avg `-0.1327` n `74`; fx avg `-0.0019` n `6`; index avg `0.0173` n `23`; metal avg `0.1796` n `18`; unknown avg `-0.0413` n `644`
- 4h: commodity avg `0.0821` n `12`; crypto_alt avg `0.0374` n `228`; crypto_major avg `0.0109` n `8`; equity avg `0.208` n `74`; fx avg `-0.0379` n `6`; index avg `0.1629` n `23`; metal avg `0.2255` n `18`; unknown avg `-2.1935` n `644`
- 24h: commodity avg `-0.7396` n `12`; crypto_alt avg `1.3911` n `228`; crypto_major avg `-0.1692` n `8`; equity avg `0.1433` n `74`; fx avg `0.0204` n `6`; index avg `0.678` n `23`; metal avg `0.6339` n `18`; unknown avg `-2.041` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
