# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T19:37:30.906354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.39` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.5959` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.0214` n `228`; crypto_major avg `0.0503` n `8`; equity avg `-0.022` n `88`; fx avg `0.0012` n `6`; index avg `0.0173` n `23`; metal avg `0.0607` n `20`; unknown avg `0.4687` n `765`
- 1h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.0395` n `228`; crypto_major avg `0.3478` n `8`; equity avg `0.1684` n `88`; fx avg `-0.0012` n `6`; index avg `0.0343` n `23`; metal avg `-0.0162` n `20`; unknown avg `0.0609` n `765`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.8716` n `228`; crypto_major avg `1.7048` n `8`; equity avg `1.4313` n `88`; fx avg `-0.0274` n `6`; index avg `0.1982` n `23`; metal avg `0.1089` n `20`; unknown avg `1.8293` n `765`
- 24h: commodity avg `-0.6133` n `12`; crypto_alt avg `1.8674` n `228`; crypto_major avg `3.1668` n `8`; equity avg `1.7069` n `88`; fx avg `0.1335` n `6`; index avg `0.2164` n `23`; metal avg `-0.4467` n `20`; unknown avg `3.4106` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
