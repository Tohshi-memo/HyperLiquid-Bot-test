# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T08:07:27.895215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.0803` n `228`; crypto_major avg `0.1326` n `8`; equity avg `0.0453` n `88`; fx avg `0.0216` n `6`; index avg `0.0007` n `23`; metal avg `0.0019` n `20`; unknown avg `0.0288` n `764`
- 1h: commodity avg `0.0582` n `12`; crypto_alt avg `0.0589` n `228`; crypto_major avg `0.231` n `8`; equity avg `0.0467` n `88`; fx avg `-0.0059` n `6`; index avg `0.0003` n `23`; metal avg `-0.0208` n `20`; unknown avg `-0.0711` n `748`
- 4h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.2834` n `228`; crypto_major avg `-0.1704` n `8`; equity avg `0.2004` n `88`; fx avg `0.0021` n `6`; index avg `0.0057` n `23`; metal avg `-0.0238` n `20`; unknown avg `-0.2736` n `716`
- 24h: commodity avg `0.0392` n `12`; crypto_alt avg `0.779` n `228`; crypto_major avg `0.5591` n `8`; equity avg `1.4223` n `87`; fx avg `0.0468` n `6`; index avg `0.0131` n `23`; metal avg `0.6854` n `20`; unknown avg `-0.206` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
