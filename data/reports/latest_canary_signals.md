# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T10:52:15.219461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `12`; crypto_alt avg `0.1684` n `228`; crypto_major avg `0.0318` n `8`; equity avg `0.1208` n `66`; fx avg `-0.0127` n `5`; index avg `0.0872` n `23`; metal avg `0.1237` n `18`; unknown avg `0.1977` n `383`
- 1h: commodity avg `0.1457` n `12`; crypto_alt avg `-0.0896` n `228`; crypto_major avg `0.11` n `8`; equity avg `-0.2732` n `66`; fx avg `-0.0002` n `5`; index avg `-0.0997` n `23`; metal avg `0.0325` n `18`; unknown avg `0.1024` n `383`
- 4h: commodity avg `-0.1168` n `12`; crypto_alt avg `-0.4545` n `228`; crypto_major avg `-0.2524` n `8`; equity avg `0.4018` n `66`; fx avg `0.0268` n `5`; index avg `0.1434` n `23`; metal avg `0.1164` n `18`; unknown avg `-0.5003` n `383`
- 24h: commodity avg `0.8337` n `12`; crypto_alt avg `-3.3881` n `228`; crypto_major avg `-1.9746` n `8`; equity avg `-0.0342` n `65`; fx avg `0.0837` n `5`; index avg `0.0894` n `23`; metal avg `-0.0171` n `18`; unknown avg `-0.5839` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
