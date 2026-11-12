# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T02:22:36.005318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `13`; crypto_alt avg `0.0592` n `239`; crypto_major avg `0.1775` n `8`; equity avg `0.2252` n `161`; fx avg `-0.0189` n `6`; index avg `0.0291` n `27`; metal avg `0.0128` n `20`; unknown avg `0.3176` n `1262`
- 1h: commodity avg `0.0901` n `13`; crypto_alt avg `0.3339` n `239`; crypto_major avg `0.3929` n `8`; equity avg `0.9097` n `161`; fx avg `-0.0403` n `6`; index avg `0.1003` n `27`; metal avg `0.0064` n `20`; unknown avg `0.0707` n `1256`
- 4h: commodity avg `0.0076` n `13`; crypto_alt avg `-1.1869` n `239`; crypto_major avg `-0.9405` n `8`; equity avg `-0.3011` n `161`; fx avg `-0.0629` n `6`; index avg `-0.0157` n `27`; metal avg `0.0207` n `20`; unknown avg `20.7093` n `1250`
- 24h: commodity avg `0.1934` n `13`; crypto_alt avg `-0.9265` n `239`; crypto_major avg `0.3673` n `8`; equity avg `2.2396` n `161`; fx avg `-0.1683` n `6`; index avg `0.2076` n `27`; metal avg `-0.239` n `20`; unknown avg `4.3659` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
