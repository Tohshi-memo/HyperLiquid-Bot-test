# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T23:07:26.296587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `-0.2038` n `236`; crypto_major avg `-0.1537` n `8`; equity avg `0.0795` n `151`; fx avg `-0.0006` n `6`; index avg `-0.0057` n `26`; metal avg `0.0014` n `20`; unknown avg `0.6245` n `1191`
- 1h: commodity avg `-0.0049` n `13`; crypto_alt avg `0.2226` n `236`; crypto_major avg `0.1858` n `8`; equity avg `0.1054` n `151`; fx avg `0.0051` n `6`; index avg `0.0056` n `26`; metal avg `0.0215` n `20`; unknown avg `0.482` n `1191`
- 4h: commodity avg `-0.0371` n `13`; crypto_alt avg `-0.9308` n `236`; crypto_major avg `-0.5543` n `8`; equity avg `-0.9647` n `151`; fx avg `0.0034` n `6`; index avg `-0.1378` n `26`; metal avg `-0.0517` n `20`; unknown avg `3.1968` n `1147`
- 24h: commodity avg `0.0144` n `13`; crypto_alt avg `-2.4741` n `236`; crypto_major avg `-1.3346` n `8`; equity avg `-0.6557` n `151`; fx avg `-0.0286` n `6`; index avg `-0.1255` n `26`; metal avg `-0.0851` n `20`; unknown avg `5.047` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.165`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
