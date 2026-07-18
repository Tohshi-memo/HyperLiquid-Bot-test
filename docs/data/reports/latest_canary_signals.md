# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T14:52:23.745413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0457` n `230`; crypto_major avg `0.0598` n `8`; equity avg `0.0181` n `96`; fx avg `-0.0085` n `6`; index avg `-0.0003` n `25`; metal avg `0.007` n `20`; unknown avg `0.0067` n `770`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `0.2651` n `230`; crypto_major avg `0.3686` n `8`; equity avg `-0.0405` n `96`; fx avg `-0.0064` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0251` n `20`; unknown avg `0.064` n `770`
- 4h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.0182` n `230`; crypto_major avg `0.2082` n `8`; equity avg `-0.0938` n `96`; fx avg `-0.0098` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.0116` n `770`
- 24h: commodity avg `0.4688` n `12`; crypto_alt avg `-0.3581` n `230`; crypto_major avg `0.6322` n `8`; equity avg `-0.0544` n `96`; fx avg `0.0087` n `6`; index avg `0.0789` n `25`; metal avg `0.1698` n `20`; unknown avg `0.0939` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
