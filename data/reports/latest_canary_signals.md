# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T17:37:28.516580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1908` n `13`; crypto_alt avg `-0.1007` n `235`; crypto_major avg `-0.0656` n `8`; equity avg `0.0114` n `143`; fx avg `-0.0024` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0098` n `20`; unknown avg `0.1074` n `1078`
- 1h: commodity avg `-0.0052` n `13`; crypto_alt avg `0.1932` n `235`; crypto_major avg `0.2778` n `8`; equity avg `0.0341` n `143`; fx avg `-0.0106` n `6`; index avg `0.0035` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.0394` n `1076`
- 4h: commodity avg `-0.0426` n `13`; crypto_alt avg `0.8882` n `235`; crypto_major avg `0.5289` n `8`; equity avg `0.0822` n `143`; fx avg `-0.0089` n `6`; index avg `0.0215` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.2316` n `950`
- 24h: commodity avg `0.1064` n `13`; crypto_alt avg `0.1821` n `235`; crypto_major avg `0.1052` n `8`; equity avg `0.2924` n `143`; fx avg `-0.0519` n `6`; index avg `0.0718` n `26`; metal avg `0.1016` n `20`; unknown avg `0.1079` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
