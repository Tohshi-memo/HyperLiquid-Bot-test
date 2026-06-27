# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T22:47:28.593862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0571` n `12`; crypto_alt avg `-0.1681` n `228`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0324` n `88`; fx avg `0.0007` n `6`; index avg `-0.0029` n `23`; metal avg `0.0045` n `20`; unknown avg `-0.1393` n `764`
- 1h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.0626` n `228`; crypto_major avg `0.0485` n `8`; equity avg `-0.0204` n `88`; fx avg `0.0049` n `6`; index avg `-0.0541` n `23`; metal avg `0.008` n `20`; unknown avg `-0.543` n `764`
- 4h: commodity avg `0.0831` n `12`; crypto_alt avg `-0.8341` n `228`; crypto_major avg `-0.7952` n `8`; equity avg `-0.0424` n `88`; fx avg `0.0055` n `6`; index avg `-0.0501` n `23`; metal avg `-0.0228` n `20`; unknown avg `-0.4677` n `764`
- 24h: commodity avg `0.1247` n `12`; crypto_alt avg `-0.673` n `228`; crypto_major avg `-0.825` n `8`; equity avg `0.3328` n `88`; fx avg `0.0132` n `6`; index avg `-0.0458` n `23`; metal avg `-0.0415` n `20`; unknown avg `-0.9173` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
