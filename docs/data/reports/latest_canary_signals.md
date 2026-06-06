# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T03:07:24.058367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0636` n `12`; crypto_alt avg `-0.8165` n `228`; crypto_major avg `-0.7108` n `8`; equity avg `-0.1144` n `74`; fx avg `-0.0065` n `6`; index avg `-0.0471` n `23`; metal avg `-0.0935` n `18`; unknown avg `-0.3341` n `425`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.6908` n `228`; crypto_major avg `-0.309` n `8`; equity avg `-0.6037` n `74`; fx avg `0.0` n `6`; index avg `-0.2157` n `23`; metal avg `-0.2622` n `18`; unknown avg `-0.3542` n `425`
- 4h: commodity avg `0.1523` n `12`; crypto_alt avg `-1.8844` n `228`; crypto_major avg `-1.2454` n `8`; equity avg `-1.7522` n `74`; fx avg `-0.0313` n `6`; index avg `-0.5207` n `23`; metal avg `-0.474` n `18`; unknown avg `1.2423` n `425`
- 24h: commodity avg `-1.2709` n `12`; crypto_alt avg `-5.0695` n `228`; crypto_major avg `-4.4687` n `8`; equity avg `-6.8306` n `74`; fx avg `-0.2116` n `6`; index avg `-4.0967` n `23`; metal avg `-3.9309` n `18`; unknown avg `0.2777` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
