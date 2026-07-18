# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T16:07:24.333881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0004` n `230`; crypto_major avg `-0.0858` n `8`; equity avg `-0.0748` n `96`; fx avg `-0.0378` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0089` n `770`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0209` n `230`; crypto_major avg `-0.1202` n `8`; equity avg `-0.1033` n `96`; fx avg `-0.0428` n `6`; index avg `-0.0076` n `25`; metal avg `-0.0241` n `20`; unknown avg `-0.0219` n `770`
- 4h: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.2162` n `230`; crypto_major avg `-0.1288` n `8`; equity avg `-0.219` n `96`; fx avg `-0.0437` n `6`; index avg `-0.0213` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.0937` n `770`
- 24h: commodity avg `0.3517` n `12`; crypto_alt avg `-0.7036` n `230`; crypto_major avg `0.201` n `8`; equity avg `-0.8639` n `96`; fx avg `-0.0889` n `6`; index avg `-0.0504` n `25`; metal avg `0.0171` n `20`; unknown avg `0.0287` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
