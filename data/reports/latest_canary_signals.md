# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T11:22:27.866463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0377` n `12`; crypto_alt avg `-0.0197` n `230`; crypto_major avg `-0.0662` n `8`; equity avg `-0.0419` n `102`; fx avg `0.0468` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0252` n `782`
- 1h: commodity avg `0.0784` n `12`; crypto_alt avg `-0.1165` n `230`; crypto_major avg `-0.0375` n `8`; equity avg `-0.1158` n `102`; fx avg `-0.0042` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.0502` n `782`
- 4h: commodity avg `0.1752` n `12`; crypto_alt avg `-0.3582` n `230`; crypto_major avg `-0.5082` n `8`; equity avg `0.0501` n `102`; fx avg `0.0052` n `6`; index avg `-0.0199` n `25`; metal avg `-0.0206` n `20`; unknown avg `-0.0725` n `782`
- 24h: commodity avg `-1.0346` n `12`; crypto_alt avg `0.3421` n `230`; crypto_major avg `0.2367` n `8`; equity avg `0.7909` n `102`; fx avg `-0.0962` n `6`; index avg `0.1847` n `25`; metal avg `0.2492` n `20`; unknown avg `0.2644` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
