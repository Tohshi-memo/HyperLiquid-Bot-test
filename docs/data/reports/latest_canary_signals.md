# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T02:52:26.007033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1856` n `228`; crypto_major avg `0.1708` n `8`; equity avg `-0.0103` n `88`; fx avg `0.0032` n `6`; index avg `0.0017` n `23`; metal avg `0.0033` n `20`; unknown avg `5.1285` n `764`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `0.7388` n `228`; crypto_major avg `0.7923` n `8`; equity avg `0.131` n `88`; fx avg `0.0047` n `6`; index avg `0.0163` n `23`; metal avg `0.0072` n `20`; unknown avg `1.3592` n `764`
- 4h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.6681` n `228`; crypto_major avg `0.5196` n `8`; equity avg `0.2145` n `88`; fx avg `-0.0067` n `6`; index avg `0.0467` n `23`; metal avg `0.0412` n `20`; unknown avg `0.5385` n `764`
- 24h: commodity avg `-0.1938` n `12`; crypto_alt avg `4.1687` n `228`; crypto_major avg `4.0212` n `8`; equity avg `2.1175` n `87`; fx avg `-0.0225` n `6`; index avg `0.1614` n `23`; metal avg `1.4698` n `20`; unknown avg `0.5951` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
