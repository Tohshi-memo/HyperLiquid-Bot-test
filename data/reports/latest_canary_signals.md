# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T05:35:57.790781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0059` n `12`; crypto_alt avg `0.1599` n `228`; crypto_major avg `-0.1273` n `8`; equity avg `-0.133` n `74`; fx avg `-0.0169` n `6`; index avg `-0.1604` n `23`; metal avg `-0.1737` n `18`; unknown avg `0.0249` n `645`
- 1h: commodity avg `0.068` n `12`; crypto_alt avg `0.472` n `228`; crypto_major avg `0.0923` n `8`; equity avg `-0.1126` n `74`; fx avg `-0.0142` n `6`; index avg `-0.0037` n `23`; metal avg `-0.106` n `18`; unknown avg `-0.274` n `645`
- 4h: commodity avg `0.073` n `12`; crypto_alt avg `1.0398` n `228`; crypto_major avg `0.4321` n `8`; equity avg `0.1726` n `74`; fx avg `0.0009` n `6`; index avg `-0.0827` n `23`; metal avg `0.0039` n `18`; unknown avg `-0.3846` n `629`
- 24h: commodity avg `-0.8315` n `12`; crypto_alt avg `3.4551` n `228`; crypto_major avg `2.9234` n `8`; equity avg `1.7877` n `74`; fx avg `0.0295` n `6`; index avg `0.787` n `23`; metal avg `2.1466` n `18`; unknown avg `3.351` n `585`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
