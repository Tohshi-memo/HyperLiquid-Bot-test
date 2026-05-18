# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T06:22:17.540431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0685` n `12`; crypto_alt avg `-0.3651` n `228`; crypto_major avg `-0.3821` n `8`; equity avg `-0.0874` n `66`; fx avg `-0.0256` n `5`; index avg `-0.0227` n `23`; metal avg `0.1393` n `18`; unknown avg `0.836` n `383`
- 1h: commodity avg `0.0436` n `12`; crypto_alt avg `-0.8192` n `228`; crypto_major avg `-0.714` n `8`; equity avg `-0.0446` n `66`; fx avg `-0.0417` n `5`; index avg `0.0434` n `23`; metal avg `-0.1187` n `18`; unknown avg `0.8151` n `363`
- 4h: commodity avg `0.0888` n `12`; crypto_alt avg `-0.7901` n `228`; crypto_major avg `-0.8678` n `8`; equity avg `-0.2494` n `66`; fx avg `-0.0636` n `5`; index avg `-0.0221` n `23`; metal avg `0.1259` n `18`; unknown avg `0.6206` n `363`
- 24h: commodity avg `2.7808` n `12`; crypto_alt avg `-11.5097` n `228`; crypto_major avg `-4.0268` n `8`; equity avg `-3.2039` n `65`; fx avg `-0.1196` n `5`; index avg `-1.7896` n `23`; metal avg `-6.1661` n `18`; unknown avg `-0.4077` n `357`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
