# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T03:22:28.003021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3154` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5393` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `-0.0612` n `239`; crypto_major avg `0.1647` n `8`; equity avg `0.2784` n `168`; fx avg `-0.0216` n `6`; index avg `0.0252` n `27`; metal avg `-0.0187` n `20`; unknown avg `0.7769` n `1261`
- 1h: commodity avg `0.034` n `13`; crypto_alt avg `0.426` n `239`; crypto_major avg `0.8979` n `8`; equity avg `0.8515` n `168`; fx avg `0.0302` n `6`; index avg `0.0736` n `27`; metal avg `0.2148` n `20`; unknown avg `0.6384` n `1255`
- 4h: commodity avg `0.1771` n `13`; crypto_alt avg `1.8192` n `239`; crypto_major avg `2.4925` n `8`; equity avg `2.6973` n `168`; fx avg `0.0097` n `6`; index avg `0.2581` n `27`; metal avg `0.9532` n `20`; unknown avg `3.9625` n `1243`
- 24h: commodity avg `0.2317` n `13`; crypto_alt avg `1.6221` n `239`; crypto_major avg `1.9293` n `8`; equity avg `2.2346` n `168`; fx avg `0.0271` n `6`; index avg `0.2241` n `27`; metal avg `0.7687` n `20`; unknown avg `183.9595` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
