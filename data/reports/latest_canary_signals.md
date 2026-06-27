# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T22:52:25.396207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.0396` n `228`; crypto_major avg `-0.0152` n `8`; equity avg `-0.0119` n `88`; fx avg `0.005` n `6`; index avg `0.0031` n `23`; metal avg `0.0093` n `20`; unknown avg `-0.1347` n `764`
- 1h: commodity avg `-0.032` n `12`; crypto_alt avg `0.1916` n `228`; crypto_major avg `0.1723` n `8`; equity avg `0.0001` n `88`; fx avg `0.0092` n `6`; index avg `-0.0481` n `23`; metal avg `0.0129` n `20`; unknown avg `-0.547` n `764`
- 4h: commodity avg `0.0939` n `12`; crypto_alt avg `-0.7068` n `228`; crypto_major avg `-0.6727` n `8`; equity avg `-0.022` n `88`; fx avg `0.0098` n `6`; index avg `-0.0441` n `23`; metal avg `-0.018` n `20`; unknown avg `-0.4809` n `764`
- 24h: commodity avg `0.1355` n `12`; crypto_alt avg `-0.5467` n `228`; crypto_major avg `-0.7029` n `8`; equity avg `0.3535` n `88`; fx avg `0.0174` n `6`; index avg `-0.0398` n `23`; metal avg `-0.0367` n `20`; unknown avg `-0.9208` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
