# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T23:07:17.613307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.1247` n `228`; crypto_major avg `-0.0863` n `8`; equity avg `-0.0264` n `65`; fx avg `0.0` n `5`; index avg `0.0214` n `23`; metal avg `-0.0008` n `18`; unknown avg `-0.0491` n `376`
- 1h: commodity avg `-0.0419` n `12`; crypto_alt avg `-0.0394` n `228`; crypto_major avg `-0.067` n `8`; equity avg `0.0281` n `65`; fx avg `0.0` n `5`; index avg `0.0348` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.3084` n `376`
- 4h: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.1064` n `228`; crypto_major avg `-0.1045` n `8`; equity avg `0.3133` n `65`; fx avg `-0.0006` n `5`; index avg `0.0968` n `23`; metal avg `0.1677` n `18`; unknown avg `-0.3159` n `376`
- 24h: commodity avg `0.3906` n `12`; crypto_alt avg `0.0965` n `228`; crypto_major avg `0.3002` n `8`; equity avg `0.7495` n `65`; fx avg `-0.0236` n `5`; index avg `0.3361` n `23`; metal avg `0.3221` n `18`; unknown avg `0.0614` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
