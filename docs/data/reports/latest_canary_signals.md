# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T19:07:27.833887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.5167` n `12`; crypto_alt avg `0.6768` n `228`; crypto_major avg `0.5512` n `8`; equity avg `0.3579` n `66`; fx avg `0.0628` n `6`; index avg `0.183` n `23`; metal avg `0.5107` n `18`; unknown avg `1.4573` n `383`
- 1h: commodity avg `-0.2545` n `12`; crypto_alt avg `0.2889` n `228`; crypto_major avg `0.1247` n `8`; equity avg `-0.0786` n `66`; fx avg `-0.0021` n `6`; index avg `0.032` n `23`; metal avg `0.3253` n `18`; unknown avg `1.2387` n `383`
- 4h: commodity avg `0.0667` n `12`; crypto_alt avg `0.6106` n `228`; crypto_major avg `0.6859` n `8`; equity avg `-0.5869` n `66`; fx avg `0.1638` n `6`; index avg `-0.3122` n `23`; metal avg `0.6444` n `18`; unknown avg `-0.1714` n `383`
- 24h: commodity avg `0.8811` n `12`; crypto_alt avg `-2.4985` n `228`; crypto_major avg `-2.5001` n `8`; equity avg `-1.3364` n `66`; fx avg `0.2016` n `6`; index avg `-0.6258` n `23`; metal avg `0.8494` n `18`; unknown avg `-0.4341` n `362`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
