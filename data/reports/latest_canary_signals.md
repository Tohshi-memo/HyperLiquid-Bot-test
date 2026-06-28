# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T03:22:24.737619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1446` n `12`; crypto_alt avg `0.1104` n `228`; crypto_major avg `0.1418` n `8`; equity avg `0.008` n `88`; fx avg `0.0001` n `6`; index avg `0.0274` n `23`; metal avg `0.0045` n `20`; unknown avg `8.9489` n `764`
- 1h: commodity avg `-0.2546` n `12`; crypto_alt avg `0.2851` n `228`; crypto_major avg `0.2925` n `8`; equity avg `0.0231` n `88`; fx avg `-0.0127` n `6`; index avg `-0.0115` n `23`; metal avg `0.0117` n `20`; unknown avg `20.9877` n `730`
- 4h: commodity avg `0.0863` n `12`; crypto_alt avg `0.3941` n `228`; crypto_major avg `0.141` n `8`; equity avg `-0.0161` n `88`; fx avg `-0.0423` n `6`; index avg `-0.0284` n `23`; metal avg `0.0576` n `20`; unknown avg `16.6643` n `722`
- 24h: commodity avg `0.2305` n `12`; crypto_alt avg `-0.8181` n `228`; crypto_major avg `-1.2202` n `8`; equity avg `0.0141` n `88`; fx avg `-0.0197` n `6`; index avg `-0.132` n `23`; metal avg `-0.0365` n `20`; unknown avg `9.9498` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2172`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
