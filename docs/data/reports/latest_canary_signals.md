# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T05:22:26.465626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.331` n `228`; crypto_major avg `0.2982` n `8`; equity avg `-0.0528` n `74`; fx avg `-0.0186` n `6`; index avg `-0.0332` n `23`; metal avg `-0.0986` n `18`; unknown avg `4352.2493` n `517`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `1.14` n `228`; crypto_major avg `0.9902` n `8`; equity avg `0.1374` n `74`; fx avg `0.0034` n `6`; index avg `0.0154` n `23`; metal avg `0.0665` n `18`; unknown avg `2901.1227` n `517`
- 4h: commodity avg `-0.1382` n `12`; crypto_alt avg `0.6876` n `228`; crypto_major avg `0.8198` n `8`; equity avg `1.1021` n `74`; fx avg `-0.0315` n `6`; index avg `0.5245` n `23`; metal avg `0.045` n `18`; unknown avg `-0.3412` n `517`
- 24h: commodity avg `-1.1678` n `12`; crypto_alt avg `1.1111` n `228`; crypto_major avg `1.6035` n `8`; equity avg `2.6342` n `74`; fx avg `-0.2376` n `6`; index avg `1.1491` n `23`; metal avg `0.3036` n `18`; unknown avg `-3.0565` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
