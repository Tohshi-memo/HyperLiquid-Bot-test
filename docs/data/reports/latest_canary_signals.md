# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T21:37:26.360866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1232` n `12`; crypto_alt avg `-0.1082` n `230`; crypto_major avg `-0.1131` n `8`; equity avg `-0.023` n `96`; fx avg `0.0` n `6`; index avg `-0.0136` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.1116` n `770`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.0663` n `230`; crypto_major avg `0.0585` n `8`; equity avg `-0.0033` n `96`; fx avg `0.0015` n `6`; index avg `-0.0193` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.2475` n `770`
- 4h: commodity avg `0.0238` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `0.3121` n `8`; equity avg `-0.0287` n `96`; fx avg `-0.0085` n `6`; index avg `-0.0395` n `25`; metal avg `-0.0224` n `20`; unknown avg `0.2931` n `770`
- 24h: commodity avg `0.1981` n `12`; crypto_alt avg `-0.2845` n `230`; crypto_major avg `0.3732` n `8`; equity avg `-0.272` n `96`; fx avg `-0.0732` n `6`; index avg `0.0141` n `25`; metal avg `0.0036` n `20`; unknown avg `0.1448` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
