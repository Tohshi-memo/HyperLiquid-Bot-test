# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T06:01:38.291650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `13`; crypto_alt avg `0.0317` n `239`; crypto_major avg `0.0364` n `8`; equity avg `0.004` n `161`; fx avg `-0.0063` n `6`; index avg `-0.0062` n `27`; metal avg `-0.0154` n `20`; unknown avg `-0.0257` n `1229`
- 1h: commodity avg `0.0714` n `13`; crypto_alt avg `-0.0112` n `239`; crypto_major avg `0.2955` n `8`; equity avg `0.3741` n `161`; fx avg `-0.0132` n `6`; index avg `0.0228` n `27`; metal avg `0.0786` n `20`; unknown avg `-0.1703` n `1223`
- 4h: commodity avg `0.0501` n `13`; crypto_alt avg `0.2488` n `239`; crypto_major avg `0.4598` n `8`; equity avg `1.452` n `161`; fx avg `-0.0648` n `6`; index avg `0.1775` n `27`; metal avg `0.2223` n `20`; unknown avg `3.4132` n `1217`
- 24h: commodity avg `0.3095` n `13`; crypto_alt avg `-0.5257` n `239`; crypto_major avg `-2.0824` n `8`; equity avg `1.5771` n `161`; fx avg `-0.1848` n `6`; index avg `0.198` n `27`; metal avg `-0.1494` n `20`; unknown avg `2.6239` n `1162`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2593`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2342`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
