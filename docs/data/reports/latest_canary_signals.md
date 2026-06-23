# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T13:22:34.471842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0819` n `12`; crypto_alt avg `0.0106` n `228`; crypto_major avg `-0.0394` n `8`; equity avg `0.0045` n `86`; fx avg `-0.0072` n `6`; index avg `-0.0118` n `23`; metal avg `-0.0706` n `20`; unknown avg `-0.0712` n `764`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `-0.3145` n `228`; crypto_major avg `-0.2964` n `8`; equity avg `-0.3834` n `86`; fx avg `0.0016` n `6`; index avg `-0.0857` n `23`; metal avg `0.0292` n `20`; unknown avg `-0.2044` n `764`
- 4h: commodity avg `-0.1473` n `12`; crypto_alt avg `-0.0961` n `228`; crypto_major avg `-0.1953` n `8`; equity avg `-0.3773` n `86`; fx avg `-0.0601` n `6`; index avg `-0.1651` n `23`; metal avg `-0.0839` n `20`; unknown avg `-0.2648` n `764`
- 24h: commodity avg `-0.4388` n `12`; crypto_alt avg `-4.8351` n `228`; crypto_major avg `-5.2008` n `8`; equity avg `-5.0184` n `85`; fx avg `-0.1761` n `6`; index avg `-1.0741` n `23`; metal avg `-1.3896` n `20`; unknown avg `-0.0384` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
