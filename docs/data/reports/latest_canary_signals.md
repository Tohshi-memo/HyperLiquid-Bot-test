# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T17:37:27.565287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1017` n `12`; crypto_alt avg `-0.0456` n `228`; crypto_major avg `-0.0199` n `8`; equity avg `-0.0751` n `74`; fx avg `0.0042` n `6`; index avg `-0.0505` n `23`; metal avg `0.0248` n `18`; unknown avg `0.5641` n `515`
- 1h: commodity avg `0.1645` n `12`; crypto_alt avg `-0.0788` n `228`; crypto_major avg `0.0651` n `8`; equity avg `-0.0061` n `74`; fx avg `0.0248` n `6`; index avg `-0.0757` n `23`; metal avg `0.0721` n `18`; unknown avg `0.6969` n `515`
- 4h: commodity avg `0.2709` n `12`; crypto_alt avg `-0.7476` n `228`; crypto_major avg `-0.6434` n `8`; equity avg `-0.0548` n `74`; fx avg `0.0603` n `6`; index avg `0.0506` n `23`; metal avg `-0.1165` n `18`; unknown avg `1.2018` n `513`
- 24h: commodity avg `0.6033` n `12`; crypto_alt avg `-2.2771` n `228`; crypto_major avg `-1.5406` n `8`; equity avg `-2.1949` n `74`; fx avg `0.0165` n `6`; index avg `-1.0891` n `23`; metal avg `-1.224` n `18`; unknown avg `-0.5865` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
