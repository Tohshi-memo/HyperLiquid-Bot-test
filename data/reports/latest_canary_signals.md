# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T03:07:28.213244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `13`; crypto_alt avg `0.0617` n `239`; crypto_major avg `0.2476` n `8`; equity avg `0.2093` n `161`; fx avg `-0.0168` n `6`; index avg `0.0271` n `27`; metal avg `0.0487` n `20`; unknown avg `2.7899` n `1257`
- 1h: commodity avg `0.0273` n `13`; crypto_alt avg `0.4187` n `239`; crypto_major avg `0.4831` n `8`; equity avg `0.6302` n `161`; fx avg `-0.0405` n `6`; index avg `0.0673` n `27`; metal avg `0.0641` n `20`; unknown avg `24.7451` n `1255`
- 4h: commodity avg `0.0358` n `13`; crypto_alt avg `0.9265` n `239`; crypto_major avg `0.6868` n `8`; equity avg `2.0584` n `161`; fx avg `-0.1021` n `6`; index avg `0.2382` n `27`; metal avg `0.296` n `20`; unknown avg `7.2988` n `1249`
- 24h: commodity avg `0.2807` n `13`; crypto_alt avg `0.0082` n `239`; crypto_major avg `-1.9439` n `8`; equity avg `0.8768` n `161`; fx avg `-0.2629` n `6`; index avg `0.1506` n `27`; metal avg `-0.2541` n `20`; unknown avg `25.4542` n `1172`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2952`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2605`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
