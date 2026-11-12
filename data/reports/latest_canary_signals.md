# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T06:07:29.633003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1769` n `13`; crypto_alt avg `-0.0465` n `239`; crypto_major avg `-0.0067` n `8`; equity avg `0.0746` n `161`; fx avg `-0.0174` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0276` n `20`; unknown avg `0.6257` n `1230`
- 1h: commodity avg `0.1945` n `13`; crypto_alt avg `-0.2864` n `239`; crypto_major avg `-0.1678` n `8`; equity avg `-0.4034` n `161`; fx avg `-0.0117` n `6`; index avg `-0.0322` n `27`; metal avg `-0.0256` n `20`; unknown avg `1.892` n `1226`
- 4h: commodity avg `0.0765` n `13`; crypto_alt avg `-0.5153` n `239`; crypto_major avg `-0.4731` n `8`; equity avg `-1.4118` n `161`; fx avg `-0.1149` n `6`; index avg `-0.1162` n `27`; metal avg `-0.093` n `20`; unknown avg `0.1397` n `1210`
- 24h: commodity avg `0.1913` n `13`; crypto_alt avg `-1.8235` n `239`; crypto_major avg `-0.9556` n `8`; equity avg `-0.7605` n `161`; fx avg `-0.2079` n `6`; index avg `-0.082` n `27`; metal avg `-0.5965` n `20`; unknown avg `1.6441` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
