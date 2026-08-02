# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T23:37:31.582593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0091` n `230`; crypto_major avg `0.0536` n `8`; equity avg `0.0106` n `102`; fx avg `-0.0261` n `6`; index avg `-0.0066` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0386` n `784`
- 1h: commodity avg `0.0658` n `12`; crypto_alt avg `-0.117` n `230`; crypto_major avg `-0.0835` n `8`; equity avg `0.1234` n `102`; fx avg `0.0298` n `6`; index avg `0.0334` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0646` n `783`
- 4h: commodity avg `0.0015` n `12`; crypto_alt avg `-0.1052` n `230`; crypto_major avg `0.1546` n `8`; equity avg `0.2486` n `102`; fx avg `0.0775` n `6`; index avg `0.0494` n `25`; metal avg `-0.0909` n `20`; unknown avg `1.8749` n `783`
- 24h: commodity avg `-1.2208` n `12`; crypto_alt avg `1.157` n `230`; crypto_major avg `1.6861` n `8`; equity avg `1.6688` n `102`; fx avg `0.0584` n `6`; index avg `0.3483` n `25`; metal avg `0.2082` n `20`; unknown avg `1.5982` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
