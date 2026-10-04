# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T17:37:26.758425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `13`; crypto_alt avg `0.0331` n `235`; crypto_major avg `0.0508` n `8`; equity avg `-0.001` n `144`; fx avg `0.0083` n `6`; index avg `-0.0014` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.0145` n `1078`
- 1h: commodity avg `0.0564` n `13`; crypto_alt avg `-0.0507` n `235`; crypto_major avg `0.0433` n `8`; equity avg `0.0139` n `144`; fx avg `0.0163` n `6`; index avg `-0.0046` n `26`; metal avg `0.006` n `20`; unknown avg `0.2261` n `1076`
- 4h: commodity avg `-0.0758` n `13`; crypto_alt avg `-0.0468` n `235`; crypto_major avg `0.129` n `8`; equity avg `0.02` n `144`; fx avg `0.0163` n `6`; index avg `-0.0232` n `26`; metal avg `-0.0072` n `20`; unknown avg `-0.0466` n `1070`
- 24h: commodity avg `0.1062` n `13`; crypto_alt avg `0.5808` n `235`; crypto_major avg `0.8224` n `8`; equity avg `0.2095` n `144`; fx avg `0.0328` n `6`; index avg `-0.0141` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.0195` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
