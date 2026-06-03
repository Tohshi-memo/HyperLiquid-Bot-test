# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T23:22:21.458288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.084` n `12`; crypto_alt avg `0.0014` n `228`; crypto_major avg `-0.0545` n `8`; equity avg `-0.0241` n `73`; fx avg `-0.0083` n `6`; index avg `-0.0868` n `23`; metal avg `0.0471` n `18`; unknown avg `-0.2426` n `419`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `-0.6568` n `228`; crypto_major avg `-0.5592` n `8`; equity avg `-0.5691` n `73`; fx avg `0.0113` n `6`; index avg `-0.1413` n `23`; metal avg `0.3544` n `18`; unknown avg `-0.0982` n `419`
- 4h: commodity avg `-0.1424` n `12`; crypto_alt avg `-0.4719` n `228`; crypto_major avg `-0.3387` n `8`; equity avg `-1.8304` n `73`; fx avg `-0.0226` n `6`; index avg `-0.5685` n `23`; metal avg `-0.0961` n `18`; unknown avg `0.9517` n `419`
- 24h: commodity avg `0.0667` n `12`; crypto_alt avg `2.0726` n `228`; crypto_major avg `-0.7151` n `8`; equity avg `-3.4386` n `72`; fx avg `0.0717` n `6`; index avg `-0.8291` n `23`; metal avg `-1.6076` n `18`; unknown avg `0.9608` n `409`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
