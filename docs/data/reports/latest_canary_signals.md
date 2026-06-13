# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T02:37:30.034923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1151` n `12`; crypto_alt avg `0.0357` n `228`; crypto_major avg `-0.0171` n `8`; equity avg `0.0168` n `74`; fx avg `-0.0184` n `6`; index avg `0.0158` n `23`; metal avg `-0.0056` n `18`; unknown avg `0.1882` n `643`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.0553` n `228`; crypto_major avg `0.0582` n `8`; equity avg `0.2188` n `74`; fx avg `-0.0179` n `6`; index avg `0.2213` n `23`; metal avg `0.005` n `18`; unknown avg `-0.3927` n `643`
- 4h: commodity avg `-0.0833` n `12`; crypto_alt avg `0.9035` n `228`; crypto_major avg `0.2066` n `8`; equity avg `0.2463` n `74`; fx avg `0.0315` n `6`; index avg `0.3101` n `23`; metal avg `0.1292` n `18`; unknown avg `-0.3626` n `643`
- 24h: commodity avg `-0.8772` n `12`; crypto_alt avg `0.1396` n `228`; crypto_major avg `-0.0208` n `8`; equity avg `-0.4607` n `74`; fx avg `-0.0086` n `6`; index avg `0.7471` n `23`; metal avg `0.5707` n `18`; unknown avg `40.3051` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
