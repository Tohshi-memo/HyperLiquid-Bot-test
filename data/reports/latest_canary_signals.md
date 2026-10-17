# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T23:04:28.484361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `13`; crypto_alt avg `-0.1023` n `236`; crypto_major avg `-0.0743` n `8`; equity avg `0.0118` n `151`; fx avg `-0.0013` n `6`; index avg `-0.0024` n `26`; metal avg `0.0014` n `20`; unknown avg `0.5208` n `1191`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `0.3246` n `236`; crypto_major avg `0.2656` n `8`; equity avg `0.0376` n `151`; fx avg `0.0043` n `6`; index avg `0.0089` n `26`; metal avg `0.0215` n `20`; unknown avg `0.3413` n `1191`
- 4h: commodity avg `-0.0405` n `13`; crypto_alt avg `-0.8304` n `236`; crypto_major avg `-0.4752` n `8`; equity avg `-1.0306` n `151`; fx avg `0.0027` n `6`; index avg `-0.1346` n `26`; metal avg `-0.0517` n `20`; unknown avg `3.1129` n `1147`
- 24h: commodity avg `0.011` n `13`; crypto_alt avg `-2.3758` n `236`; crypto_major avg `-1.2562` n `8`; equity avg `-0.7223` n `151`; fx avg `-0.0294` n `6`; index avg `-0.1222` n `26`; metal avg `-0.0851` n `20`; unknown avg `4.9754` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.165`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
