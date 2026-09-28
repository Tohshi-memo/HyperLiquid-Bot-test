# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T01:07:30.704588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.2056` n `234`; crypto_major avg `-0.2726` n `8`; equity avg `-0.2352` n `141`; fx avg `0.0027` n `6`; index avg `-0.0624` n `26`; metal avg `-0.1141` n `20`; unknown avg `-0.1156` n `960`
- 1h: commodity avg `-0.0828` n `12`; crypto_alt avg `0.0333` n `234`; crypto_major avg `-0.081` n `8`; equity avg `-0.5305` n `141`; fx avg `0.0338` n `6`; index avg `-0.0979` n `26`; metal avg `-0.2757` n `20`; unknown avg `56.8723` n `960`
- 4h: commodity avg `-0.4229` n `12`; crypto_alt avg `0.2658` n `234`; crypto_major avg `-0.3538` n `8`; equity avg `-0.7781` n `141`; fx avg `0.1077` n `6`; index avg `-0.0911` n `26`; metal avg `-0.4726` n `20`; unknown avg `1.8899` n `888`
- 24h: commodity avg `-0.4822` n `12`; crypto_alt avg `1.1952` n `234`; crypto_major avg `-0.0004` n `8`; equity avg `-0.4558` n `141`; fx avg `0.0464` n `6`; index avg `-0.0517` n `26`; metal avg `-0.4867` n `20`; unknown avg `10.9145` n `829`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
