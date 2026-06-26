# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T19:22:31.549136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `-0.1102` n `228`; crypto_major avg `-0.1141` n `8`; equity avg `-0.0466` n `88`; fx avg `0.0008` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0242` n `20`; unknown avg `-0.0668` n `764`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.0248` n `228`; crypto_major avg `-0.1181` n `8`; equity avg `-0.1443` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0374` n `23`; metal avg `-0.0581` n `20`; unknown avg `0.1111` n `764`
- 4h: commodity avg `0.0412` n `12`; crypto_alt avg `1.1059` n `228`; crypto_major avg `0.7911` n `8`; equity avg `0.1622` n `87`; fx avg `-0.0083` n `6`; index avg `0.0024` n `23`; metal avg `-0.1196` n `20`; unknown avg `-0.352` n `764`
- 24h: commodity avg `-0.6473` n `12`; crypto_alt avg `3.1651` n `228`; crypto_major avg `2.9814` n `8`; equity avg `-0.2224` n `87`; fx avg `-0.0793` n `6`; index avg `-0.2394` n `23`; metal avg `0.4343` n `20`; unknown avg `0.0969` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
