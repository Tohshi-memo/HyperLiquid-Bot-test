# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T10:52:30.795923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2566` n `13`; crypto_alt avg `0.1539` n `234`; crypto_major avg `0.2015` n `8`; equity avg `0.2102` n `142`; fx avg `-0.0022` n `6`; index avg `0.0458` n `26`; metal avg `0.0365` n `20`; unknown avg `-0.076` n `975`
- 1h: commodity avg `-0.2653` n `13`; crypto_alt avg `-0.1816` n `234`; crypto_major avg `0.2232` n `8`; equity avg `0.2685` n `142`; fx avg `-0.0227` n `6`; index avg `0.0814` n `26`; metal avg `0.1496` n `20`; unknown avg `-0.1058` n `973`
- 4h: commodity avg `-0.1067` n `13`; crypto_alt avg `-1.3484` n `234`; crypto_major avg `-0.5734` n `8`; equity avg `-0.3414` n `142`; fx avg `-0.0328` n `6`; index avg `-0.0495` n `26`; metal avg `-0.1321` n `20`; unknown avg `7.1798` n `957`
- 24h: commodity avg `-0.4195` n `13`; crypto_alt avg `-0.8053` n `234`; crypto_major avg `0.0308` n `8`; equity avg `0.6936` n `142`; fx avg `0.0372` n `6`; index avg `0.221` n `26`; metal avg `-0.1822` n `20`; unknown avg `774.6658` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
