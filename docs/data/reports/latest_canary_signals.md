# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T08:01:50.893018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.1147` n `228`; crypto_major avg `-0.1011` n `8`; equity avg `-0.0673` n `66`; fx avg `-0.0106` n `6`; index avg `-0.0475` n `23`; metal avg `0.032` n `18`; unknown avg `0.1012` n `383`
- 1h: commodity avg `-0.1809` n `12`; crypto_alt avg `0.1291` n `228`; crypto_major avg `0.2042` n `8`; equity avg `0.212` n `66`; fx avg `0.0091` n `6`; index avg `0.0905` n `23`; metal avg `0.1099` n `18`; unknown avg `0.1286` n `383`
- 4h: commodity avg `0.1587` n `12`; crypto_alt avg `0.2713` n `228`; crypto_major avg `0.2513` n `8`; equity avg `0.5716` n `66`; fx avg `-0.0006` n `6`; index avg `0.318` n `23`; metal avg `0.2598` n `18`; unknown avg `0.4145` n `363`
- 24h: commodity avg `0.7058` n `12`; crypto_alt avg `1.8271` n `228`; crypto_major avg `0.9949` n `8`; equity avg `-0.7798` n `66`; fx avg `0.3085` n `6`; index avg `-0.2906` n `23`; metal avg `0.171` n `18`; unknown avg `0.9719` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
