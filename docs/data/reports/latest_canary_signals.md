# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T16:52:24.523484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `0.0177` n `230`; crypto_major avg `0.121` n `8`; equity avg `0.116` n `102`; fx avg `0.001` n `6`; index avg `0.0203` n `25`; metal avg `0.0187` n `20`; unknown avg `0.0542` n `782`
- 1h: commodity avg `-0.0943` n `12`; crypto_alt avg `0.0192` n `230`; crypto_major avg `0.3137` n `8`; equity avg `0.1814` n `102`; fx avg `0.0004` n `6`; index avg `0.0361` n `25`; metal avg `0.0403` n `20`; unknown avg `0.1986` n `782`
- 4h: commodity avg `-0.136` n `12`; crypto_alt avg `0.0502` n `230`; crypto_major avg `0.5343` n `8`; equity avg `0.2086` n `102`; fx avg `-0.0632` n `6`; index avg `0.057` n `25`; metal avg `0.0624` n `20`; unknown avg `1.2749` n `782`
- 24h: commodity avg `-1.2674` n `12`; crypto_alt avg `0.306` n `230`; crypto_major avg `0.5131` n `8`; equity avg `1.1778` n `102`; fx avg `-0.1541` n `6`; index avg `0.269` n `25`; metal avg `0.298` n `20`; unknown avg `1.4718` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
