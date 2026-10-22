# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T15:07:28.614961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0521` n `13`; crypto_alt avg `-0.2559` n `237`; crypto_major avg `-0.2057` n `8`; equity avg `-0.1977` n `151`; fx avg `0.0266` n `6`; index avg `0.0114` n `26`; metal avg `-0.0961` n `20`; unknown avg `-0.0603` n `1191`
- 1h: commodity avg `0.0443` n `13`; crypto_alt avg `-0.7884` n `237`; crypto_major avg `-0.1795` n `8`; equity avg `-1.3533` n `151`; fx avg `0.0081` n `6`; index avg `-0.1789` n `26`; metal avg `-0.0438` n `20`; unknown avg `-0.1535` n `1135`
- 4h: commodity avg `0.0724` n `13`; crypto_alt avg `-0.8433` n `237`; crypto_major avg `-0.1952` n `8`; equity avg `-1.5493` n `151`; fx avg `0.0669` n `6`; index avg `-0.1294` n `26`; metal avg `-0.1046` n `20`; unknown avg `-0.1753` n `1095`
- 24h: commodity avg `-0.3246` n `13`; crypto_alt avg `-3.0973` n `237`; crypto_major avg `-1.9463` n `8`; equity avg `-3.4414` n `151`; fx avg `-0.1327` n `6`; index avg `-0.4459` n `26`; metal avg `-0.6857` n `20`; unknown avg `0.7837` n `866`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
