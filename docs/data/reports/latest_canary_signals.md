# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T00:43:11.001034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `0.2087` n `236`; crypto_major avg `0.2179` n `8`; equity avg `0.4518` n `151`; fx avg `0.0529` n `6`; index avg `0.0772` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.3819` n `1136`
- 1h: commodity avg `0.0351` n `13`; crypto_alt avg `0.4571` n `236`; crypto_major avg `0.2647` n `8`; equity avg `-0.1726` n `151`; fx avg `0.0661` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0676` n `20`; unknown avg `1.2911` n `1128`
- 4h: commodity avg `-0.0605` n `13`; crypto_alt avg `-0.0523` n `236`; crypto_major avg `-0.2823` n `8`; equity avg `-0.6558` n `151`; fx avg `0.0443` n `6`; index avg `-0.125` n `26`; metal avg `-0.1362` n `20`; unknown avg `0.1041` n `1090`
- 24h: commodity avg `-0.1615` n `13`; crypto_alt avg `0.8047` n `236`; crypto_major avg `0.5369` n `8`; equity avg `0.8571` n `151`; fx avg `0.082` n `6`; index avg `0.1202` n `26`; metal avg `0.1964` n `20`; unknown avg `25.2209` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0929`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0791`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0636`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0575`, n `666`, weak_sample_signal
