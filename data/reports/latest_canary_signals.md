# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T09:07:27.638264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.2214` n `239`; crypto_major avg `-0.2033` n `8`; equity avg `-0.0575` n `161`; fx avg `0.0076` n `6`; index avg `0.0022` n `27`; metal avg `-0.0784` n `20`; unknown avg `0.7793` n `1258`
- 1h: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.2065` n `239`; crypto_major avg `-0.2735` n `8`; equity avg `-0.0412` n `161`; fx avg `-0.0101` n `6`; index avg `0.0138` n `27`; metal avg `-0.2312` n `20`; unknown avg `0.5709` n `1256`
- 4h: commodity avg `0.3677` n `13`; crypto_alt avg `-0.4972` n `239`; crypto_major avg `-0.3518` n `8`; equity avg `-0.1398` n `161`; fx avg `0.0867` n `6`; index avg `-0.0303` n `27`; metal avg `-0.2672` n `20`; unknown avg `60.8954` n `1206`
- 24h: commodity avg `0.4117` n `13`; crypto_alt avg `-1.5582` n `239`; crypto_major avg `-0.8082` n `8`; equity avg `-0.8923` n `161`; fx avg `-0.0478` n `6`; index avg `-0.0978` n `27`; metal avg `-0.8665` n `20`; unknown avg `18.6275` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
