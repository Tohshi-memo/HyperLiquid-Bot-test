# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T07:37:15.687003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.247` n `12`; crypto_alt avg `0.1974` n `228`; crypto_major avg `0.2404` n `8`; equity avg `0.1973` n `66`; fx avg `-0.0368` n `5`; index avg `0.0927` n `23`; metal avg `0.3484` n `18`; unknown avg `1.0017` n `383`
- 1h: commodity avg `-0.52` n `12`; crypto_alt avg `-0.1282` n `228`; crypto_major avg `0.0297` n `8`; equity avg `0.3173` n `66`; fx avg `-0.0265` n `5`; index avg `0.1297` n `23`; metal avg `0.4858` n `18`; unknown avg `0.8009` n `383`
- 4h: commodity avg `-0.3501` n `12`; crypto_alt avg `-0.6594` n `228`; crypto_major avg `-0.4152` n `8`; equity avg `0.3792` n `66`; fx avg `-0.057` n `5`; index avg `0.108` n `23`; metal avg `0.8573` n `18`; unknown avg `0.6699` n `363`
- 24h: commodity avg `0.4752` n `12`; crypto_alt avg `-3.0598` n `228`; crypto_major avg `-1.4817` n `8`; equity avg `0.0465` n `65`; fx avg `0.0284` n `5`; index avg `0.1327` n `23`; metal avg `0.1384` n `18`; unknown avg `0.5265` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
