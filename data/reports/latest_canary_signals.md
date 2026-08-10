# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:01:23.911424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1252` n `230`; crypto_major avg `-0.0609` n `8`; equity avg `-0.0758` n `113`; fx avg `0.0022` n `6`; index avg `-0.005` n `25`; metal avg `0.0106` n `20`; unknown avg `-0.0516` n `785`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.0035` n `8`; equity avg `-0.1603` n `113`; fx avg `0.0015` n `6`; index avg `-0.0255` n `25`; metal avg `0.0458` n `20`; unknown avg `-0.0703` n `785`
- 4h: commodity avg `0.0313` n `12`; crypto_alt avg `-0.4161` n `230`; crypto_major avg `-0.0621` n `8`; equity avg `-0.5557` n `113`; fx avg `0.0159` n `6`; index avg `-0.0498` n `25`; metal avg `0.071` n `20`; unknown avg `2.8639` n `785`
- 24h: commodity avg `0.8441` n `12`; crypto_alt avg `-0.9837` n `230`; crypto_major avg `-0.865` n `8`; equity avg `-1.8095` n `113`; fx avg `0.255` n `6`; index avg `-0.0845` n `25`; metal avg `0.3617` n `20`; unknown avg `103.6246` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
