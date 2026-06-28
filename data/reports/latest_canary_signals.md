# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T11:22:24.417281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0379` n `12`; crypto_alt avg `0.0533` n `228`; crypto_major avg `0.1157` n `8`; equity avg `0.0146` n `88`; fx avg `-0.0037` n `6`; index avg `0.0027` n `23`; metal avg `-0.0016` n `20`; unknown avg `0.0548` n `764`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `0.1157` n `228`; crypto_major avg `0.2029` n `8`; equity avg `0.0397` n `88`; fx avg `0.004` n `6`; index avg `0.0053` n `23`; metal avg `-0.0036` n `20`; unknown avg `-0.283` n `764`
- 4h: commodity avg `-0.0791` n `12`; crypto_alt avg `0.2734` n `228`; crypto_major avg `0.4269` n `8`; equity avg `0.2133` n `88`; fx avg `0.0198` n `6`; index avg `0.0573` n `23`; metal avg `0.0168` n `20`; unknown avg `2.3887` n `742`
- 24h: commodity avg `0.1952` n `12`; crypto_alt avg `0.1296` n `228`; crypto_major avg `-0.4718` n `8`; equity avg `0.1184` n `88`; fx avg `-0.0026` n `6`; index avg `-0.0443` n `23`; metal avg `-0.0124` n `20`; unknown avg `20.1984` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
