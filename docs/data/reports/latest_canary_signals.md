# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T03:37:31.469431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.017` n `230`; crypto_major avg `-0.0181` n `8`; equity avg `0.0133` n `102`; fx avg `-0.0084` n `6`; index avg `-0.002` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.111` n `784`
- 1h: commodity avg `-0.0765` n `12`; crypto_alt avg `-0.1796` n `230`; crypto_major avg `-0.1972` n `8`; equity avg `-0.1947` n `102`; fx avg `0.043` n `6`; index avg `-0.0299` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.205` n `784`
- 4h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.7261` n `230`; crypto_major avg `-0.82` n `8`; equity avg `0.176` n `102`; fx avg `-0.2799` n `6`; index avg `-0.0752` n `25`; metal avg `-0.1114` n `20`; unknown avg `-0.035` n `784`
- 24h: commodity avg `-0.0989` n `12`; crypto_alt avg `-0.6742` n `230`; crypto_major avg `-0.4344` n `8`; equity avg `0.8663` n `102`; fx avg `-0.2396` n `6`; index avg `0.0185` n `25`; metal avg `-0.0645` n `20`; unknown avg `1.2851` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
