# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T12:52:40.276608+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.6616` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.093` n `12`; crypto_alt avg `0.2224` n `233`; crypto_major avg `0.5889` n `8`; equity avg `0.352` n `136`; fx avg `-0.046` n `6`; index avg `0.0778` n `26`; metal avg `0.2328` n `20`; unknown avg `-0.4818` n `796`
- 1h: commodity avg `0.0874` n `12`; crypto_alt avg `1.7774` n `233`; crypto_major avg `1.9283` n `8`; equity avg `0.6883` n `136`; fx avg `-0.0369` n `6`; index avg `0.0994` n `26`; metal avg `0.2667` n `20`; unknown avg `0.8729` n `788`
- 4h: commodity avg `-0.0625` n `12`; crypto_alt avg `0.7166` n `233`; crypto_major avg `1.1918` n `8`; equity avg `0.5067` n `136`; fx avg `-0.0859` n `6`; index avg `0.1034` n `26`; metal avg `0.1547` n `20`; unknown avg `0.5074` n `788`
- 24h: commodity avg `-0.1032` n `12`; crypto_alt avg `1.0518` n `233`; crypto_major avg `1.6629` n `8`; equity avg `1.0934` n `136`; fx avg `-0.1268` n `6`; index avg `0.2561` n `26`; metal avg `0.1647` n `20`; unknown avg `2.2044` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
