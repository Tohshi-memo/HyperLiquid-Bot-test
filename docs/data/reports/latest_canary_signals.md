# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T12:07:29.618949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.1615` n `228`; crypto_major avg `-0.1963` n `8`; equity avg `-0.0928` n `74`; fx avg `0.0121` n `6`; index avg `-0.0055` n `23`; metal avg `0.0073` n `18`; unknown avg `0.0412` n `645`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0498` n `228`; crypto_major avg `0.0114` n `8`; equity avg `0.0401` n `74`; fx avg `0.0404` n `6`; index avg `0.0582` n `23`; metal avg `0.0359` n `18`; unknown avg `0.1602` n `645`
- 4h: commodity avg `0.2209` n `12`; crypto_alt avg `-0.0237` n `228`; crypto_major avg `0.225` n `8`; equity avg `0.2378` n `74`; fx avg `0.0187` n `6`; index avg `0.1245` n `23`; metal avg `-0.0315` n `18`; unknown avg `0.4118` n `629`
- 24h: commodity avg `-0.5187` n `12`; crypto_alt avg `-0.3137` n `228`; crypto_major avg `0.5738` n `8`; equity avg `0.9761` n `74`; fx avg `0.004` n `6`; index avg `0.2643` n `23`; metal avg `0.0475` n `18`; unknown avg `-0.9922` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
