# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T13:52:33.973059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3997` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.3196` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `2.2113` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.9598` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0862` n `12`; crypto_alt avg `0.6124` n `234`; crypto_major avg `1.7037` n `8`; equity avg `-0.062` n `140`; fx avg `0.0048` n `6`; index avg `-0.0143` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.7044` n `908`
- 1h: commodity avg `0.2977` n `12`; crypto_alt avg `0.9587` n `234`; crypto_major avg `2.1135` n `8`; equity avg `0.1537` n `140`; fx avg `0.0038` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0978` n `20`; unknown avg `3.2328` n `906`
- 4h: commodity avg `0.3728` n `12`; crypto_alt avg `0.8579` n `234`; crypto_major avg `2.1425` n `8`; equity avg `-0.2572` n `140`; fx avg `-0.0576` n `6`; index avg `-0.0784` n `26`; metal avg `-0.1771` n `20`; unknown avg `1.9055` n `897`
- 24h: commodity avg `0.3254` n `12`; crypto_alt avg `6.4997` n `234`; crypto_major avg `6.077` n `8`; equity avg `0.6232` n `140`; fx avg `0.223` n `6`; index avg `-0.0481` n `26`; metal avg `0.0592` n `20`; unknown avg `392.1306` n `743`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
