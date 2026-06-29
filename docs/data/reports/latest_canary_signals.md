# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T16:22:26.218814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.1792` n `228`; crypto_major avg `-0.3628` n `8`; equity avg `0.0063` n `88`; fx avg `0.0003` n `6`; index avg `0.0241` n `23`; metal avg `-0.1533` n `20`; unknown avg `0.3254` n `765`
- 1h: commodity avg `0.1121` n `12`; crypto_alt avg `0.5801` n `228`; crypto_major avg `0.3965` n `8`; equity avg `0.9215` n `88`; fx avg `0.0034` n `6`; index avg `0.1341` n `23`; metal avg `-0.0083` n `20`; unknown avg `0.7927` n `765`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.7538` n `228`; crypto_major avg `-0.8906` n `8`; equity avg `-0.0925` n `88`; fx avg `0.0512` n `6`; index avg `0.0011` n `23`; metal avg `-0.2631` n `20`; unknown avg `0.5789` n `764`
- 24h: commodity avg `-0.5949` n `12`; crypto_alt avg `0.0371` n `228`; crypto_major avg `0.1906` n `8`; equity avg `0.6828` n `88`; fx avg `0.1256` n `6`; index avg `0.093` n `23`; metal avg `-0.6163` n `20`; unknown avg `1.7558` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
