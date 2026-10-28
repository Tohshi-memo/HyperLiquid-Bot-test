# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T06:37:29.753763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0495` n `13`; crypto_alt avg `-0.1053` n `238`; crypto_major avg `-0.0709` n `8`; equity avg `0.0655` n `154`; fx avg `0.0038` n `6`; index avg `0.0011` n `27`; metal avg `-0.0184` n `20`; unknown avg `1.2142` n `1236`
- 1h: commodity avg `0.0758` n `13`; crypto_alt avg `0.0176` n `238`; crypto_major avg `0.0632` n `8`; equity avg `0.1098` n `154`; fx avg `-0.0154` n `6`; index avg `0.0035` n `27`; metal avg `-0.021` n `20`; unknown avg `3.287` n `1216`
- 4h: commodity avg `0.1247` n `13`; crypto_alt avg `-0.1329` n `238`; crypto_major avg `0.0177` n `8`; equity avg `0.5386` n `154`; fx avg `-0.0437` n `6`; index avg `0.0269` n `27`; metal avg `-0.1123` n `20`; unknown avg `86.8446` n `1200`
- 24h: commodity avg `0.0304` n `13`; crypto_alt avg `2.0566` n `237`; crypto_major avg `2.1406` n `8`; equity avg `3.9369` n `154`; fx avg `0.054` n `6`; index avg `0.5105` n `27`; metal avg `0.3332` n `20`; unknown avg `93.577` n `1016`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
