# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T10:22:25.460649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0609` n `230`; crypto_major avg `-0.0095` n `8`; equity avg `-0.0043` n `96`; fx avg `0.0061` n `6`; index avg `0.01` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0014` n `769`
- 1h: commodity avg `0.0865` n `12`; crypto_alt avg `0.2108` n `230`; crypto_major avg `0.0984` n `8`; equity avg `0.0082` n `96`; fx avg `0.0039` n `6`; index avg `-0.0044` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0278` n `769`
- 4h: commodity avg `0.1458` n `12`; crypto_alt avg `-0.3115` n `230`; crypto_major avg `-0.0872` n `8`; equity avg `-0.1114` n `96`; fx avg `0.0121` n `6`; index avg `0.0274` n `25`; metal avg `0.031` n `20`; unknown avg `-0.1122` n `769`
- 24h: commodity avg `0.6759` n `12`; crypto_alt avg `-0.6826` n `230`; crypto_major avg `0.0344` n `8`; equity avg `0.5307` n `96`; fx avg `0.0183` n `6`; index avg `0.1678` n `25`; metal avg `0.1803` n `20`; unknown avg `0.2187` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
