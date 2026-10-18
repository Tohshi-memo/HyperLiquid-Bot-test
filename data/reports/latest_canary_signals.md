# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T22:22:23.885129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `13`; crypto_alt avg `0.2366` n `237`; crypto_major avg `0.0895` n `8`; equity avg `0.0713` n `151`; fx avg `0.0042` n `6`; index avg `0.012` n `26`; metal avg `0.0428` n `20`; unknown avg `1.0348` n `1186`
- 1h: commodity avg `-0.3046` n `13`; crypto_alt avg `1.5866` n `237`; crypto_major avg `1.3093` n `8`; equity avg `1.0353` n `151`; fx avg `0.0455` n `6`; index avg `0.2669` n `26`; metal avg `0.2209` n `20`; unknown avg `2.4835` n `1110`
- 4h: commodity avg `-0.2554` n `13`; crypto_alt avg `0.4695` n `237`; crypto_major avg `1.0004` n `8`; equity avg `0.9169` n `151`; fx avg `-0.0121` n `6`; index avg `0.2493` n `26`; metal avg `0.191` n `20`; unknown avg `10.0257` n `1088`
- 24h: commodity avg `-0.2407` n `13`; crypto_alt avg `-2.1111` n `236`; crypto_major avg `0.158` n `8`; equity avg `0.8625` n `151`; fx avg `-0.0031` n `6`; index avg `0.2346` n `26`; metal avg `0.2181` n `20`; unknown avg `2.0471` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2012`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1424`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.134`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
