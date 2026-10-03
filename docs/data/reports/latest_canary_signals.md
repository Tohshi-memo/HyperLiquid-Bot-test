# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T16:22:25.368741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1723` n `13`; crypto_alt avg `-0.0288` n `235`; crypto_major avg `-0.0385` n `8`; equity avg `0.0121` n `143`; fx avg `0.0044` n `6`; index avg `0.0029` n `26`; metal avg `0.0` n `20`; unknown avg `-0.0353` n `1078`
- 1h: commodity avg `-0.1141` n `13`; crypto_alt avg `0.1246` n `235`; crypto_major avg `-0.0989` n `8`; equity avg `0.0337` n `143`; fx avg `0.0032` n `6`; index avg `0.0113` n `26`; metal avg `0.0142` n `20`; unknown avg `-0.0627` n `1070`
- 4h: commodity avg `0.0673` n `13`; crypto_alt avg `0.6927` n `235`; crypto_major avg `0.17` n `8`; equity avg `0.0428` n `143`; fx avg `-0.0028` n `6`; index avg `0.0224` n `26`; metal avg `0.0046` n `20`; unknown avg `0.211` n `950`
- 24h: commodity avg `0.3634` n `13`; crypto_alt avg `-1.3558` n `235`; crypto_major avg `-0.791` n `8`; equity avg `-0.0509` n `143`; fx avg `-0.0245` n `6`; index avg `0.0249` n `26`; metal avg `0.1079` n `20`; unknown avg `-0.0196` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
