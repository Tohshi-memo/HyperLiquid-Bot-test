# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T07:37:30.978859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `0.3388` n `228`; crypto_major avg `0.2353` n `8`; equity avg `0.0785` n `74`; fx avg `0.0001` n `6`; index avg `-0.0275` n `23`; metal avg `0.0079` n `18`; unknown avg `0.0354` n `643`
- 1h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.7196` n `228`; crypto_major avg `0.4012` n `8`; equity avg `0.1918` n `74`; fx avg `0.0017` n `6`; index avg `0.0109` n `23`; metal avg `0.0677` n `18`; unknown avg `-0.0084` n `643`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `0.9602` n `228`; crypto_major avg `0.5306` n `8`; equity avg `-0.0032` n `74`; fx avg `0.0133` n `6`; index avg `-0.0215` n `23`; metal avg `0.0334` n `18`; unknown avg `-0.0309` n `619`
- 24h: commodity avg `-0.5713` n `12`; crypto_alt avg `1.9375` n `228`; crypto_major avg `1.1574` n `8`; equity avg `0.2555` n `74`; fx avg `0.0194` n `6`; index avg `1.1253` n `23`; metal avg `1.1146` n `18`; unknown avg `33.4631` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
