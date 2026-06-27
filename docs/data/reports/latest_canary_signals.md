# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T19:07:29.501166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.096` n `228`; crypto_major avg `0.0568` n `8`; equity avg `0.0275` n `88`; fx avg `0.0006` n `6`; index avg `0.0011` n `23`; metal avg `0.0013` n `20`; unknown avg `0.0067` n `764`
- 1h: commodity avg `-0.0224` n `12`; crypto_alt avg `0.1516` n `228`; crypto_major avg `-0.0003` n `8`; equity avg `0.0405` n `88`; fx avg `0.0006` n `6`; index avg `-0.0104` n `23`; metal avg `-0.004` n `20`; unknown avg `-0.1651` n `764`
- 4h: commodity avg `-0.1633` n `12`; crypto_alt avg `-0.4165` n `228`; crypto_major avg `-0.7386` n `8`; equity avg `-0.1322` n `88`; fx avg `-0.0033` n `6`; index avg `-0.0424` n `23`; metal avg `-0.0297` n `20`; unknown avg `0.0373` n `764`
- 24h: commodity avg `0.2837` n `12`; crypto_alt avg `-0.2512` n `228`; crypto_major avg `-0.3438` n `8`; equity avg `0.6209` n `88`; fx avg `0.0794` n `6`; index avg `-0.0558` n `23`; metal avg `0.0924` n `20`; unknown avg `-0.1606` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
