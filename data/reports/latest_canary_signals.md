# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T10:52:29.616818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0411` n `13`; crypto_alt avg `-0.1371` n `239`; crypto_major avg `-0.2014` n `8`; equity avg `-0.2675` n `162`; fx avg `0.0013` n `6`; index avg `-0.0219` n `27`; metal avg `0.0018` n `20`; unknown avg `0.3597` n `1267`
- 1h: commodity avg `-0.033` n `13`; crypto_alt avg `0.0376` n `239`; crypto_major avg `0.0515` n `8`; equity avg `-0.1677` n `162`; fx avg `0.0056` n `6`; index avg `-0.0157` n `27`; metal avg `0.0167` n `20`; unknown avg `0.6565` n `1255`
- 4h: commodity avg `-0.0499` n `13`; crypto_alt avg `0.1844` n `239`; crypto_major avg `0.3706` n `8`; equity avg `0.6035` n `162`; fx avg `0.0385` n `6`; index avg `0.0649` n `27`; metal avg `-0.1352` n `20`; unknown avg `0.2273` n `1237`
- 24h: commodity avg `-0.1293` n `13`; crypto_alt avg `-1.799` n `239`; crypto_major avg `-1.0331` n `8`; equity avg `-0.9611` n `162`; fx avg `-0.1183` n `6`; index avg `-0.0575` n `27`; metal avg `-0.8787` n `20`; unknown avg `0.1768` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
