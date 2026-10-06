# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T02:37:29.241919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `13`; crypto_alt avg `-0.2353` n `235`; crypto_major avg `-0.1297` n `8`; equity avg `-0.1078` n `149`; fx avg `-0.0036` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0355` n `20`; unknown avg `-0.2019` n `1074`
- 1h: commodity avg `0.0544` n `13`; crypto_alt avg `-0.5677` n `235`; crypto_major avg `-0.2973` n `8`; equity avg `-0.0971` n `149`; fx avg `-0.031` n `6`; index avg `-0.0309` n `26`; metal avg `-0.0901` n `20`; unknown avg `-0.1978` n `1072`
- 4h: commodity avg `0.0884` n `13`; crypto_alt avg `-1.3815` n `235`; crypto_major avg `-0.6392` n `8`; equity avg `-0.2202` n `149`; fx avg `-0.0017` n `6`; index avg `-0.0605` n `26`; metal avg `-0.1437` n `20`; unknown avg `0.3354` n `1066`
- 24h: commodity avg `0.0036` n `13`; crypto_alt avg `-1.416` n `235`; crypto_major avg `-0.7301` n `8`; equity avg `-0.182` n `149`; fx avg `-0.007` n `6`; index avg `0.0384` n `26`; metal avg `-0.1143` n `20`; unknown avg `630.8219` n `793`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
