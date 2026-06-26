# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T23:07:29.712237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.1183` n `228`; crypto_major avg `0.154` n `8`; equity avg `0.0017` n `88`; fx avg `-0.0264` n `6`; index avg `-0.0024` n `23`; metal avg `0.0052` n `20`; unknown avg `-0.0063` n `764`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `0.2922` n `228`; crypto_major avg `0.4572` n `8`; equity avg `0.0938` n `88`; fx avg `-0.0169` n `6`; index avg `-0.0004` n `23`; metal avg `0.0385` n `20`; unknown avg `-0.0023` n `748`
- 4h: commodity avg `0.2575` n `12`; crypto_alt avg `-0.4014` n `228`; crypto_major avg `-0.2188` n `8`; equity avg `0.2255` n `88`; fx avg `0.0447` n `6`; index avg `-0.0635` n `23`; metal avg `0.1153` n `20`; unknown avg `-0.0727` n `748`
- 24h: commodity avg `-0.2568` n `12`; crypto_alt avg `1.6984` n `228`; crypto_major avg `1.6439` n `8`; equity avg `-0.1974` n `87`; fx avg `-0.0087` n `6`; index avg `-0.3312` n `23`; metal avg `0.7329` n `20`; unknown avg `0.1463` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
