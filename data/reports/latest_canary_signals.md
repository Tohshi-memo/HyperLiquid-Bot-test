# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T00:07:13.160389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.4177` n `228`; crypto_major avg `-0.1857` n `8`; equity avg `-0.0111` n `65`; fx avg `0.0204` n `5`; index avg `0.0009` n `23`; metal avg `0.0216` n `18`; unknown avg `-0.0193` n `376`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.6606` n `228`; crypto_major avg `-0.2964` n `8`; equity avg `0.0617` n `65`; fx avg `0.0298` n `5`; index avg `0.0198` n `23`; metal avg `-0.0009` n `18`; unknown avg `0.3119` n `376`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.7293` n `228`; crypto_major avg `-0.3736` n `8`; equity avg `0.2446` n `65`; fx avg `0.0289` n `5`; index avg `0.1118` n `23`; metal avg `0.1183` n `18`; unknown avg `-0.0068` n `376`
- 24h: commodity avg `0.5582` n `12`; crypto_alt avg `-0.5976` n `228`; crypto_major avg `0.0342` n `8`; equity avg `0.7857` n `65`; fx avg `0.0055` n `5`; index avg `0.2488` n `23`; metal avg `0.382` n `18`; unknown avg `0.3216` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
