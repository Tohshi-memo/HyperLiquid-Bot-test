# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T01:22:19.400297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `-0.5007` n `228`; crypto_major avg `-0.3753` n `8`; equity avg `-0.0254` n `69`; fx avg `-0.0066` n `6`; index avg `0.0497` n `23`; metal avg `0.3835` n `18`; unknown avg `0.0199` n `417`
- 1h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.1379` n `228`; crypto_major avg `-0.3395` n `8`; equity avg `-0.2107` n `69`; fx avg `0.0326` n `6`; index avg `-0.0907` n `23`; metal avg `0.4016` n `18`; unknown avg `-0.0226` n `417`
- 4h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.3997` n `228`; crypto_major avg `-0.4784` n `8`; equity avg `0.2595` n `69`; fx avg `0.0764` n `6`; index avg `-0.0281` n `23`; metal avg `0.544` n `18`; unknown avg `-0.3889` n `417`
- 24h: commodity avg `0.5036` n `12`; crypto_alt avg `-1.2576` n `228`; crypto_major avg `0.2864` n `8`; equity avg `2.4283` n `69`; fx avg `0.0638` n `6`; index avg `0.8327` n `23`; metal avg `1.668` n `18`; unknown avg `0.01` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
