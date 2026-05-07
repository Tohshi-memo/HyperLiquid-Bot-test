# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T15:11:34.275732+00:00`
- Correlation status: `ready`
- Asset price records: `560`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2584` n `12`; crypto_alt avg `-0.0705` n `228`; crypto_major avg `0.0242` n `8`; equity avg `-0.265` n `65`; fx avg `0.0041` n `5`; index avg `0.0266` n `23`; metal avg `-0.0937` n `18`; unknown avg `-0.0101` n `365`
- 1h: commodity avg `0.8141` n `12`; crypto_alt avg `-0.4186` n `228`; crypto_major avg `-0.2458` n `8`; equity avg `0.0283` n `65`; fx avg `-0.0034` n `5`; index avg `0.2826` n `23`; metal avg `0.2631` n `18`; unknown avg `-0.1239` n `365`
- 4h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.6644` n `228`; crypto_major avg `-1.0108` n `8`; equity avg `-0.617` n `65`; fx avg `-0.0134` n `5`; index avg `-0.2141` n `23`; metal avg `0.3825` n `18`; unknown avg `-0.4426` n `365`
- 24h: commodity avg `-0.7719` n `12`; crypto_alt avg `0.4508` n `228`; crypto_major avg `-1.6948` n `8`; equity avg `0.8194` n `65`; fx avg `0.114` n `5`; index avg `0.4107` n `23`; metal avg `1.7945` n `18`; unknown avg `-0.0551` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1328`, n `556`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `556`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `556`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0996`, n `556`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `556`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `552`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `552`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `552`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `556`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0749`, n `552`, weak_sample_signal
