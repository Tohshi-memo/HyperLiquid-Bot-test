# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T22:52:26.671996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1772` n `228`; crypto_major avg `0.1313` n `8`; equity avg `0.0557` n `88`; fx avg `0.0068` n `6`; index avg `0.004` n `23`; metal avg `0.0245` n `20`; unknown avg `0.0606` n `764`
- 1h: commodity avg `-0.0` n `12`; crypto_alt avg `-0.1106` n `228`; crypto_major avg `0.0227` n `8`; equity avg `0.1121` n `88`; fx avg `-0.0146` n `6`; index avg `0.0026` n `23`; metal avg `0.0255` n `20`; unknown avg `-0.1345` n `748`
- 4h: commodity avg `0.2262` n `12`; crypto_alt avg `-0.0448` n `228`; crypto_major avg `0.1873` n `8`; equity avg `0.563` n `88`; fx avg `0.0695` n `6`; index avg `-0.0482` n `23`; metal avg `0.1138` n `20`; unknown avg `0.0764` n `748`
- 24h: commodity avg `-0.2604` n `12`; crypto_alt avg `1.5546` n `228`; crypto_major avg `1.4778` n `8`; equity avg `-0.1308` n `87`; fx avg `0.0166` n `6`; index avg `-0.326` n `23`; metal avg `0.7586` n `20`; unknown avg `0.1006` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
