# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T02:37:30.923690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1826` n `12`; crypto_alt avg `0.1479` n `228`; crypto_major avg `0.1025` n `8`; equity avg `-0.0241` n `74`; fx avg `0.0069` n `6`; index avg `-0.0389` n `23`; metal avg `-0.1236` n `18`; unknown avg `0.0177` n `557`
- 1h: commodity avg `0.1659` n `12`; crypto_alt avg `0.574` n `228`; crypto_major avg `0.6496` n `8`; equity avg `0.2728` n `74`; fx avg `0.0057` n `6`; index avg `0.1079` n `23`; metal avg `0.1887` n `18`; unknown avg `0.1084` n `557`
- 4h: commodity avg `0.5115` n `12`; crypto_alt avg `0.261` n `228`; crypto_major avg `0.1554` n `8`; equity avg `0.2072` n `74`; fx avg `-0.0147` n `6`; index avg `-0.1713` n `23`; metal avg `-0.1127` n `18`; unknown avg `-0.1888` n `556`
- 24h: commodity avg `-2.1818` n `12`; crypto_alt avg `3.4669` n `228`; crypto_major avg `3.5239` n `8`; equity avg `4.4913` n `74`; fx avg `-0.0247` n `6`; index avg `2.2353` n `23`; metal avg `3.2835` n `18`; unknown avg `2.5151` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
