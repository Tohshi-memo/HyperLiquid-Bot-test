# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T03:37:32.538352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `12`; crypto_alt avg `-0.0265` n `228`; crypto_major avg `-0.1339` n `8`; equity avg `-0.0627` n `86`; fx avg `0.0032` n `6`; index avg `-0.0047` n `23`; metal avg `-0.0364` n `20`; unknown avg `-0.1545` n `765`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.2709` n `228`; crypto_major avg `-0.3601` n `8`; equity avg `-0.0153` n `86`; fx avg `-0.0232` n `6`; index avg `0.0177` n `23`; metal avg `-0.0984` n `20`; unknown avg `-0.3443` n `764`
- 4h: commodity avg `-0.1155` n `12`; crypto_alt avg `-0.3637` n `228`; crypto_major avg `-0.4482` n `8`; equity avg `-0.8125` n `86`; fx avg `0.0566` n `6`; index avg `-0.0626` n `23`; metal avg `-0.4205` n `20`; unknown avg `0.2518` n `748`
- 24h: commodity avg `-0.4417` n `12`; crypto_alt avg `-2.2678` n `228`; crypto_major avg `-2.049` n `8`; equity avg `-0.0904` n `86`; fx avg `0.0647` n `6`; index avg `0.5956` n `23`; metal avg `-1.6458` n `20`; unknown avg `-0.5193` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
