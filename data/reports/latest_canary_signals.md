# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T19:52:31.026578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1387` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0863` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0585` n `228`; crypto_major avg `0.2458` n `8`; equity avg `0.0076` n `88`; fx avg `0.001` n `6`; index avg `-0.0062` n `23`; metal avg `-0.0612` n `20`; unknown avg `-0.1871` n `765`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.0502` n `228`; crypto_major avg `0.6462` n `8`; equity avg `0.0779` n `88`; fx avg `-0.0009` n `6`; index avg `0.0127` n `23`; metal avg `-0.0672` n `20`; unknown avg `-0.1535` n `765`
- 4h: commodity avg `-0.0703` n `12`; crypto_alt avg `0.8087` n `228`; crypto_major avg `2.0684` n `8`; equity avg `1.3153` n `88`; fx avg `-0.0092` n `6`; index avg `0.156` n `23`; metal avg `-0.0179` n `20`; unknown avg `1.0041` n `765`
- 24h: commodity avg `-0.6575` n `12`; crypto_alt avg `2.1548` n `228`; crypto_major avg `3.7275` n `8`; equity avg `1.7346` n `88`; fx avg `0.145` n `6`; index avg `0.2121` n `23`; metal avg `-0.4902` n `20`; unknown avg `3.1684` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
