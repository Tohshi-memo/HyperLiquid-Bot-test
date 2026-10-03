# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T18:52:31.368841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0509` n `13`; crypto_alt avg `-0.0827` n `235`; crypto_major avg `-0.0448` n `8`; equity avg `-0.0055` n `143`; fx avg `-0.0018` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.1223` n `1078`
- 1h: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.2675` n `235`; crypto_major avg `-0.0807` n `8`; equity avg `0.0064` n `143`; fx avg `-0.0081` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.5006` n `1076`
- 4h: commodity avg `-0.0522` n `13`; crypto_alt avg `-0.1232` n `235`; crypto_major avg `0.1645` n `8`; equity avg `0.093` n `143`; fx avg `-0.014` n `6`; index avg `0.0264` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.4056` n `1014`
- 24h: commodity avg `0.1661` n `13`; crypto_alt avg `2.5563` n `235`; crypto_major avg `1.5515` n `8`; equity avg `0.2536` n `143`; fx avg `-0.0547` n `6`; index avg `0.0746` n `26`; metal avg `0.042` n `20`; unknown avg `0.7658` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1686`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
