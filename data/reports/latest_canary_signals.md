# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T23:52:31.759471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.0413` n `234`; crypto_major avg `-0.0802` n `8`; equity avg `-0.0419` n `141`; fx avg `-0.0134` n `6`; index avg `-0.021` n `26`; metal avg `-0.0234` n `20`; unknown avg `5.277` n `946`
- 1h: commodity avg `-0.0705` n `12`; crypto_alt avg `0.2188` n `234`; crypto_major avg `0.1644` n `8`; equity avg `-0.0535` n `141`; fx avg `0.0296` n `6`; index avg `-0.006` n `26`; metal avg `-0.0212` n `20`; unknown avg `10.4073` n `944`
- 4h: commodity avg `-0.469` n `12`; crypto_alt avg `-0.1859` n `234`; crypto_major avg `-0.4323` n `8`; equity avg `-0.1239` n `141`; fx avg `-0.0093` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0665` n `20`; unknown avg `15.8832` n `858`
- 24h: commodity avg `0.6059` n `12`; crypto_alt avg `3.8129` n `234`; crypto_major avg `0.9155` n `8`; equity avg `-0.3361` n `141`; fx avg `0.0526` n `6`; index avg `-0.1065` n `26`; metal avg `-0.1242` n `20`; unknown avg `29.6715` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
