# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T20:52:26.955109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-0.1462` n `234`; crypto_major avg `-0.0967` n `8`; equity avg `-0.0218` n `141`; fx avg `-0.0041` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.4352` n `962`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.2625` n `234`; crypto_major avg `-0.2328` n `8`; equity avg `-0.016` n `141`; fx avg `-0.0169` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0021` n `20`; unknown avg `2.6528` n `954`
- 4h: commodity avg `0.0561` n `12`; crypto_alt avg `0.4834` n `234`; crypto_major avg `0.2643` n `8`; equity avg `0.1241` n `141`; fx avg `-0.0215` n `6`; index avg `0.0187` n `26`; metal avg `0.0054` n `20`; unknown avg `3.7126` n `928`
- 24h: commodity avg `-0.08` n `12`; crypto_alt avg `1.7244` n `234`; crypto_major avg `0.8873` n `8`; equity avg `0.4604` n `141`; fx avg `-0.026` n `6`; index avg `0.0465` n `26`; metal avg `-0.009` n `20`; unknown avg `7.8323` n `871`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
