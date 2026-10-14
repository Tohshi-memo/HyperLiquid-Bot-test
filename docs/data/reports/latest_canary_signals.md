# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T22:07:27.284710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `0.0692` n `236`; crypto_major avg `-0.1103` n `8`; equity avg `0.0269` n `151`; fx avg `-0.0175` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.0828` n `1078`
- 1h: commodity avg `0.0383` n `13`; crypto_alt avg `0.3991` n `236`; crypto_major avg `0.1613` n `8`; equity avg `-0.1444` n `151`; fx avg `-0.0176` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0127` n `20`; unknown avg `-0.113` n `1052`
- 4h: commodity avg `-0.0315` n `13`; crypto_alt avg `0.5521` n `236`; crypto_major avg `0.1737` n `8`; equity avg `-0.5299` n `151`; fx avg `-0.0059` n `6`; index avg `-0.0603` n `26`; metal avg `0.0125` n `20`; unknown avg `1.3828` n `998`
- 24h: commodity avg `-0.1045` n `13`; crypto_alt avg `-2.1999` n `236`; crypto_major avg `-2.1018` n `8`; equity avg `-4.5779` n `151`; fx avg `-0.1515` n `6`; index avg `-0.6043` n `26`; metal avg `-0.8553` n `20`; unknown avg `1392.5111` n `890`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0694`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0524`, n `666`, weak_sample_signal
