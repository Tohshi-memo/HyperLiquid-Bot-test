# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T19:52:26.459568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5124` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5121` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.259` n `228`; crypto_major avg `0.1758` n `8`; equity avg `-0.0182` n `88`; fx avg `0.001` n `6`; index avg `-0.0014` n `23`; metal avg `0.0` n `20`; unknown avg `0.0074` n `764`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.7158` n `228`; crypto_major avg `-0.6252` n `8`; equity avg `-0.116` n `88`; fx avg `0.0` n `6`; index avg `-0.0163` n `23`; metal avg `-0.0352` n `20`; unknown avg `0.1633` n `764`
- 4h: commodity avg `-0.0851` n `12`; crypto_alt avg `-1.4974` n `228`; crypto_major avg `-1.5912` n `8`; equity avg `-0.2679` n `88`; fx avg `0.0101` n `6`; index avg `-0.0791` n `23`; metal avg `-0.0788` n `20`; unknown avg `0.5005` n `764`
- 24h: commodity avg `0.1941` n `12`; crypto_alt avg `-0.9942` n `228`; crypto_major avg `-1.1157` n `8`; equity avg `0.4035` n `88`; fx avg `0.0896` n `6`; index avg `-0.0533` n `23`; metal avg `0.0117` n `20`; unknown avg `-0.3089` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
