# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T20:37:34.842254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `0.0743` n `239`; crypto_major avg `0.2046` n `8`; equity avg `0.0047` n `168`; fx avg `0.0021` n `6`; index avg `0.0024` n `27`; metal avg `0.008` n `20`; unknown avg `2.5099` n `1263`
- 1h: commodity avg `-0.0138` n `13`; crypto_alt avg `0.029` n `239`; crypto_major avg `0.2261` n `8`; equity avg `0.038` n `168`; fx avg `0.0026` n `6`; index avg `0.0056` n `27`; metal avg `0.0369` n `20`; unknown avg `1.1923` n `1253`
- 4h: commodity avg `-0.0181` n `13`; crypto_alt avg `0.9491` n `239`; crypto_major avg `1.3634` n `8`; equity avg `0.4101` n `168`; fx avg `-0.0138` n `6`; index avg `0.0351` n `27`; metal avg `0.0061` n `20`; unknown avg `22.8111` n `1205`
- 24h: commodity avg `0.1658` n `13`; crypto_alt avg `2.0727` n `239`; crypto_major avg `1.5634` n `8`; equity avg `2.2219` n `168`; fx avg `-0.035` n `6`; index avg `0.186` n `27`; metal avg `0.2276` n `20`; unknown avg `13.2379` n `1025`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
