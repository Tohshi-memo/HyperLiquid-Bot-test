# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T13:22:33.375994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `13`; crypto_alt avg `0.0967` n `239`; crypto_major avg `0.0294` n `8`; equity avg `0.0411` n `168`; fx avg `0.0089` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0457` n `20`; unknown avg `0.2614` n `1263`
- 1h: commodity avg `-0.0043` n `13`; crypto_alt avg `-0.3667` n `239`; crypto_major avg `-0.0543` n `8`; equity avg `0.0573` n `168`; fx avg `-0.0227` n `6`; index avg `0.0162` n `27`; metal avg `-0.01` n `20`; unknown avg `49.9799` n `1261`
- 4h: commodity avg `0.3127` n `13`; crypto_alt avg `-1.1652` n `239`; crypto_major avg `-0.2849` n `8`; equity avg `-0.6686` n `168`; fx avg `0.0087` n `6`; index avg `-0.1182` n `27`; metal avg `-0.1042` n `20`; unknown avg `201.1929` n `1189`
- 24h: commodity avg `0.4833` n `13`; crypto_alt avg `-1.5916` n `239`; crypto_major avg `-2.6571` n `8`; equity avg `-4.6954` n `168`; fx avg `-0.0503` n `6`; index avg `-0.3855` n `27`; metal avg `-1.0898` n `20`; unknown avg `462.6641` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
