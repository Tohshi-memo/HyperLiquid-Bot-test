# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T14:22:33.617198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `13`; crypto_alt avg `-0.0501` n `239`; crypto_major avg `0.0564` n `8`; equity avg `-0.0802` n `162`; fx avg `0.0074` n `6`; index avg `-0.0119` n `27`; metal avg `0.0193` n `20`; unknown avg `-0.0075` n `1264`
- 1h: commodity avg `0.0239` n `13`; crypto_alt avg `-0.2121` n `239`; crypto_major avg `0.0075` n `8`; equity avg `-0.0503` n `162`; fx avg `0.0244` n `6`; index avg `-0.0086` n `27`; metal avg `0.0347` n `20`; unknown avg `7.594` n `1262`
- 4h: commodity avg `0.2699` n `13`; crypto_alt avg `1.1103` n `239`; crypto_major avg `1.2817` n `8`; equity avg `1.4038` n `162`; fx avg `0.054` n `6`; index avg `0.086` n `27`; metal avg `0.0815` n `20`; unknown avg `9.8907` n `1218`
- 24h: commodity avg `-0.2085` n `13`; crypto_alt avg `1.4763` n `239`; crypto_major avg `1.8118` n `8`; equity avg `-1.1763` n `162`; fx avg `-0.0369` n `6`; index avg `-0.1669` n `27`; metal avg `-0.0728` n `20`; unknown avg `13.192` n `1107`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
