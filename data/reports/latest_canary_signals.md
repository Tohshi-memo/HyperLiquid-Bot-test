# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T04:52:23.621108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0307` n `12`; crypto_alt avg `-0.1887` n `228`; crypto_major avg `-0.1639` n `8`; equity avg `-0.0983` n `73`; fx avg `0.0084` n `6`; index avg `0.0251` n `23`; metal avg `-0.0527` n `18`; unknown avg `-0.616` n `420`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.9317` n `228`; crypto_major avg `-0.3962` n `8`; equity avg `0.1434` n `73`; fx avg `0.0009` n `6`; index avg `0.0866` n `23`; metal avg `0.3628` n `18`; unknown avg `-0.5096` n `420`
- 4h: commodity avg `-0.256` n `12`; crypto_alt avg `-2.0534` n `228`; crypto_major avg `0.4248` n `8`; equity avg `0.2454` n `73`; fx avg `0.0194` n `6`; index avg `0.0876` n `23`; metal avg `0.4243` n `18`; unknown avg `-0.3764` n `419`
- 24h: commodity avg `-0.0702` n `12`; crypto_alt avg `-2.0957` n `228`; crypto_major avg `-1.7358` n `8`; equity avg `-3.4831` n `73`; fx avg `0.0065` n `6`; index avg `-1.0173` n `23`; metal avg `-1.2671` n `18`; unknown avg `0.2004` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
