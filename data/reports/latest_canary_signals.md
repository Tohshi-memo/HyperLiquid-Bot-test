# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T03:37:29.581167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `13`; crypto_alt avg `0.4783` n `239`; crypto_major avg `0.5034` n `8`; equity avg `0.3464` n `162`; fx avg `-0.0124` n `6`; index avg `0.0195` n `27`; metal avg `-0.0448` n `20`; unknown avg `0.2409` n `1262`
- 1h: commodity avg `-0.0022` n `13`; crypto_alt avg `0.9932` n `239`; crypto_major avg `1.0205` n `8`; equity avg `0.8301` n `162`; fx avg `0.0044` n `6`; index avg `0.0497` n `27`; metal avg `0.0606` n `20`; unknown avg `-0.172` n `1258`
- 4h: commodity avg `-0.1511` n `13`; crypto_alt avg `1.2411` n `239`; crypto_major avg `0.8819` n `8`; equity avg `1.5011` n `162`; fx avg `0.0389` n `6`; index avg `0.11` n `27`; metal avg `0.2717` n `20`; unknown avg `161.7764` n `1254`
- 24h: commodity avg `-0.9954` n `13`; crypto_alt avg `0.8521` n `239`; crypto_major avg `1.2757` n `8`; equity avg `-2.0467` n `162`; fx avg `-0.0491` n `6`; index avg `-0.1883` n `27`; metal avg `-0.0049` n `20`; unknown avg `556.4751` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
