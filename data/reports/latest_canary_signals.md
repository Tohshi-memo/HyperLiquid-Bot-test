# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T12:21:35.839750+00:00`
- Correlation status: `ready`
- Asset price records: `549`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2237` n `12`; crypto_alt avg `0.2486` n `228`; crypto_major avg `0.1146` n `8`; equity avg `0.0014` n `65`; fx avg `-0.0082` n `5`; index avg `-0.0357` n `23`; metal avg `0.1146` n `18`; unknown avg `0.0641` n `365`
- 1h: commodity avg `-0.2265` n `12`; crypto_alt avg `0.4271` n `228`; crypto_major avg `0.1453` n `8`; equity avg `0.0517` n `65`; fx avg `-0.0143` n `5`; index avg `0.0137` n `23`; metal avg `0.4666` n `18`; unknown avg `-0.0515` n `365`
- 4h: commodity avg `-0.873` n `12`; crypto_alt avg `0.432` n `228`; crypto_major avg `-0.1714` n `8`; equity avg `0.0207` n `65`; fx avg `0.0182` n `5`; index avg `-0.1695` n `23`; metal avg `0.4359` n `18`; unknown avg `0.2939` n `357`
- 24h: commodity avg `-1.2496` n `7`; crypto_alt avg `0.5358` n `223`; crypto_major avg `-2.3055` n `7`; equity avg `0.5361` n `47`; fx avg `0.0977` n `4`; index avg `0.3739` n `6`; metal avg `1.8595` n `7`; unknown avg `1.1705` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.133`, n `545`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `545`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1044`, n `545`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0803`, n `541`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `541`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0762`, n `541`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `541`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0691`, n `545`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `545`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.067`, n `541`, weak_sample_signal
