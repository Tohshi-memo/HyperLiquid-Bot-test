# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T00:07:27.876324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.27` n `12`; crypto_alt avg `0.4859` n `228`; crypto_major avg `0.3265` n `8`; equity avg `0.2674` n `74`; fx avg `0.0369` n `6`; index avg `-0.0051` n `23`; metal avg `0.1149` n `18`; unknown avg `0.0773` n `556`
- 1h: commodity avg `0.3437` n `12`; crypto_alt avg `0.5058` n `228`; crypto_major avg `0.4511` n `8`; equity avg `0.4045` n `74`; fx avg `0.0147` n `6`; index avg `0.1194` n `23`; metal avg `-0.0441` n `18`; unknown avg `0.1586` n `556`
- 4h: commodity avg `0.0673` n `12`; crypto_alt avg `0.3208` n `228`; crypto_major avg `0.1983` n `8`; equity avg `0.7017` n `74`; fx avg `0.0712` n `6`; index avg `0.3104` n `23`; metal avg `0.2251` n `18`; unknown avg `-0.1962` n `556`
- 24h: commodity avg `-2.6681` n `12`; crypto_alt avg `4.2515` n `228`; crypto_major avg `4.398` n `8`; equity avg `5.3832` n `74`; fx avg `0.0921` n `6`; index avg `2.6834` n `23`; metal avg `4.5378` n `18`; unknown avg `2.7889` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
