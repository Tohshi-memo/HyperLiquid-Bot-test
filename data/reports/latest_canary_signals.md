# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T12:07:29.241428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0492` n `13`; crypto_alt avg `0.0936` n `239`; crypto_major avg `-0.0161` n `8`; equity avg `-0.1804` n `168`; fx avg `0.0223` n `6`; index avg `-0.0015` n `27`; metal avg `-0.0431` n `20`; unknown avg `0.1292` n `1243`
- 1h: commodity avg `-0.0501` n `13`; crypto_alt avg `0.0886` n `239`; crypto_major avg `-0.0645` n `8`; equity avg `-0.7717` n `168`; fx avg `0.0091` n `6`; index avg `-0.061` n `27`; metal avg `-0.1405` n `20`; unknown avg `0.8558` n `1245`
- 4h: commodity avg `-0.2606` n `13`; crypto_alt avg `-0.0476` n `239`; crypto_major avg `-0.2236` n `8`; equity avg `-0.5177` n `168`; fx avg `0.005` n `6`; index avg `-0.0386` n `27`; metal avg `-0.1121` n `20`; unknown avg `381.8492` n `1133`
- 24h: commodity avg `0.0779` n `13`; crypto_alt avg `1.5968` n `239`; crypto_major avg `2.5798` n `8`; equity avg `2.8874` n `168`; fx avg `-0.0704` n `6`; index avg `0.2085` n `27`; metal avg `1.0543` n `20`; unknown avg `66.1441` n `1023`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
