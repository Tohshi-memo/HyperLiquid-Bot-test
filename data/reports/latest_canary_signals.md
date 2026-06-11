# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T22:37:27.867831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0694` n `12`; crypto_alt avg `-0.0683` n `228`; crypto_major avg `-0.0652` n `8`; equity avg `0.022` n `74`; fx avg `0.043` n `6`; index avg `-0.0204` n `23`; metal avg `0.0645` n `18`; unknown avg `-0.0331` n `556`
- 1h: commodity avg `-0.2514` n `12`; crypto_alt avg `-0.245` n `228`; crypto_major avg `0.0648` n `8`; equity avg `0.2971` n `74`; fx avg `0.0327` n `6`; index avg `0.2894` n `23`; metal avg `0.1055` n `18`; unknown avg `7.5904` n `556`
- 4h: commodity avg `-1.4043` n `12`; crypto_alt avg `0.2004` n `228`; crypto_major avg `0.1592` n `8`; equity avg `1.3245` n `74`; fx avg `0.0732` n `6`; index avg `0.863` n `23`; metal avg `0.9798` n `18`; unknown avg `0.9926` n `556`
- 24h: commodity avg `-2.837` n `12`; crypto_alt avg `4.9501` n `228`; crypto_major avg `4.6321` n `8`; equity avg `4.8136` n `74`; fx avg `0.1527` n `6`; index avg `2.7792` n `23`; metal avg `3.7977` n `18`; unknown avg `2.2031` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
