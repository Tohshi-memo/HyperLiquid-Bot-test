# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T19:37:30.895515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8006` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5912` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.848` n `228`; crypto_major avg `-0.6463` n `8`; equity avg `-0.1121` n `88`; fx avg `0.0` n `6`; index avg `-0.0101` n `23`; metal avg `-0.0285` n `20`; unknown avg `0.0885` n `764`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.9701` n `228`; crypto_major avg `-0.8921` n `8`; equity avg `-0.1161` n `88`; fx avg `-0.0017` n `6`; index avg `-0.007` n `23`; metal avg `-0.0344` n `20`; unknown avg `0.1526` n `764`
- 4h: commodity avg `-0.1212` n `12`; crypto_alt avg `-1.7746` n `228`; crypto_major avg `-1.8623` n `8`; equity avg `-0.2711` n `88`; fx avg `-0.006` n `6`; index avg `-0.0617` n `23`; metal avg `-0.0838` n `20`; unknown avg `0.722` n `764`
- 24h: commodity avg `0.2112` n `12`; crypto_alt avg `-1.2726` n `228`; crypto_major avg `-1.2726` n `8`; equity avg `0.4729` n `88`; fx avg `0.0842` n `6`; index avg `-0.0546` n `23`; metal avg `0.0522` n `20`; unknown avg `-0.367` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
