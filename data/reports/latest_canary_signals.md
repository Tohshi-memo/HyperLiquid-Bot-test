# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T09:07:48.809411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0781` n `13`; crypto_alt avg `-0.3957` n `239`; crypto_major avg `-0.4449` n `8`; equity avg `-0.3168` n `162`; fx avg `-0.0084` n `6`; index avg `-0.0293` n `27`; metal avg `0.0268` n `20`; unknown avg `8.377` n `1259`
- 1h: commodity avg `-0.1946` n `13`; crypto_alt avg `-0.418` n `239`; crypto_major avg `-0.5455` n `8`; equity avg `-0.264` n `162`; fx avg `0.0042` n `6`; index avg `-0.0124` n `27`; metal avg `0.0441` n `20`; unknown avg `10.5311` n `1261`
- 4h: commodity avg `-0.1365` n `13`; crypto_alt avg `-0.8088` n `239`; crypto_major avg `-0.6196` n `8`; equity avg `-0.3673` n `162`; fx avg `-0.0086` n `6`; index avg `0.021` n `27`; metal avg `0.0243` n `20`; unknown avg `13.7144` n `1077`
- 24h: commodity avg `-0.4608` n `13`; crypto_alt avg `-1.4468` n `239`; crypto_major avg `-1.4537` n `8`; equity avg `-0.8382` n `162`; fx avg `-0.0465` n `6`; index avg `-0.0393` n `27`; metal avg `0.0245` n `20`; unknown avg `14.1647` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
