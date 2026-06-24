# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T07:52:27.427458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.0325` n `228`; crypto_major avg `0.0429` n `8`; equity avg `0.0584` n `86`; fx avg `-0.0018` n `6`; index avg `0.0222` n `23`; metal avg `0.0339` n `20`; unknown avg `-0.0083` n `764`
- 1h: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.3475` n `228`; crypto_major avg `-0.3112` n `8`; equity avg `-0.1699` n `86`; fx avg `-0.0286` n `6`; index avg `-0.0205` n `23`; metal avg `-0.103` n `20`; unknown avg `-0.1295` n `756`
- 4h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0896` n `228`; crypto_major avg `0.0047` n `8`; equity avg `0.46` n `86`; fx avg `0.0677` n `6`; index avg `0.1689` n `23`; metal avg `0.1173` n `20`; unknown avg `-0.1129` n `732`
- 24h: commodity avg `-0.4085` n `12`; crypto_alt avg `-0.7922` n `228`; crypto_major avg `-1.1154` n `8`; equity avg `4.6134` n `86`; fx avg `-0.0513` n `6`; index avg `0.0482` n `23`; metal avg `-0.133` n `20`; unknown avg `-0.295` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
