# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T22:07:27.230113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2482` n `12`; crypto_alt avg `-0.0805` n `228`; crypto_major avg `-0.0707` n `8`; equity avg `0.0544` n `73`; fx avg `-0.0146` n `6`; index avg `-0.0154` n `23`; metal avg `-0.146` n `18`; unknown avg `0.8704` n `419`
- 1h: commodity avg `-0.429` n `12`; crypto_alt avg `1.2115` n `228`; crypto_major avg `0.9212` n `8`; equity avg `-0.3472` n `73`; fx avg `-0.0368` n `6`; index avg `-0.21` n `23`; metal avg `0.0206` n `18`; unknown avg `0.304` n `419`
- 4h: commodity avg `0.0973` n `12`; crypto_alt avg `0.1892` n `228`; crypto_major avg `0.0235` n `8`; equity avg `-1.4459` n `73`; fx avg `-0.0305` n `6`; index avg `-0.4868` n `23`; metal avg `-0.3266` n `18`; unknown avg `0.8709` n `419`
- 24h: commodity avg `0.7608` n `12`; crypto_alt avg `2.0545` n `228`; crypto_major avg `-0.6321` n `8`; equity avg `-3.521` n `72`; fx avg `0.0356` n `6`; index avg `-0.8544` n `23`; metal avg `-2.3433` n `18`; unknown avg `0.6009` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
