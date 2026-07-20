# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T18:22:27.352695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9341` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1093` n `12`; crypto_alt avg `0.0489` n `230`; crypto_major avg `0.0391` n `8`; equity avg `-0.0467` n `98`; fx avg `0.0125` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.0184` n `770`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `0.2091` n `230`; crypto_major avg `0.2998` n `8`; equity avg `0.0313` n `98`; fx avg `0.0174` n `6`; index avg `0.0018` n `25`; metal avg `-0.0372` n `20`; unknown avg `-0.0058` n `770`
- 4h: commodity avg `0.1128` n `12`; crypto_alt avg `1.6489` n `230`; crypto_major avg `2.0411` n `8`; equity avg `0.8117` n `98`; fx avg `-0.0542` n `6`; index avg `0.0292` n `25`; metal avg `0.107` n `20`; unknown avg `1.2842` n `770`
- 24h: commodity avg `-0.3471` n `12`; crypto_alt avg `2.1801` n `230`; crypto_major avg `1.8973` n `8`; equity avg `0.72` n `98`; fx avg `-0.1373` n `6`; index avg `0.1971` n `25`; metal avg `0.1447` n `20`; unknown avg `0.5181` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0984`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `666`, weak_sample_signal
