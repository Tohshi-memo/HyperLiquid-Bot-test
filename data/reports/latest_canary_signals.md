# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T13:22:39.220595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0901` n `13`; crypto_alt avg `-0.0165` n `235`; crypto_major avg `0.0543` n `8`; equity avg `0.0665` n `144`; fx avg `-0.0238` n `6`; index avg `0.0215` n `26`; metal avg `0.0052` n `20`; unknown avg `0.5544` n `1079`
- 1h: commodity avg `-0.203` n `13`; crypto_alt avg `-0.143` n `235`; crypto_major avg `-0.0609` n `8`; equity avg `0.0653` n `144`; fx avg `0.0055` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0322` n `20`; unknown avg `1.1297` n `1077`
- 4h: commodity avg `-0.2575` n `13`; crypto_alt avg `-0.0912` n `235`; crypto_major avg `-0.114` n `8`; equity avg `-0.0676` n `144`; fx avg `-0.0032` n `6`; index avg `0.0135` n `26`; metal avg `-0.0866` n `20`; unknown avg `39.6154` n `1071`
- 24h: commodity avg `-0.4045` n `13`; crypto_alt avg `0.8326` n `235`; crypto_major avg `0.8723` n `8`; equity avg `0.1296` n `144`; fx avg `-0.0578` n `6`; index avg `-0.0401` n `26`; metal avg `0.2753` n `20`; unknown avg `0.7954` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2142`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
