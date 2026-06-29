# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T19:07:32.585331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.2681` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2215` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.1174` n `228`; crypto_major avg `-0.0365` n `8`; equity avg `-0.0699` n `88`; fx avg `-0.0012` n `6`; index avg `-0.007` n `23`; metal avg `-0.074` n `20`; unknown avg `0.4774` n `765`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.3628` n `228`; crypto_major avg `-0.293` n `8`; equity avg `0.1153` n `88`; fx avg `-0.0076` n `6`; index avg `0.0279` n `23`; metal avg `-0.0867` n `20`; unknown avg `0.4866` n `765`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `1.5072` n `228`; crypto_major avg `2.2763` n `8`; equity avg `1.6903` n `88`; fx avg `-0.0204` n `6`; index avg `0.2235` n `23`; metal avg `0.0548` n `20`; unknown avg `2.3636` n `765`
- 24h: commodity avg `-0.6333` n `12`; crypto_alt avg `1.6609` n `228`; crypto_major avg `2.5726` n `8`; equity avg `1.5685` n `88`; fx avg `0.1277` n `6`; index avg `0.1916` n `23`; metal avg `-0.5147` n `20`; unknown avg `1.7315` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
