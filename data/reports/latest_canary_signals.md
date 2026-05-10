# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T01:24:17.446516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.219` n `228`; crypto_major avg `-0.1214` n `8`; equity avg `0.0387` n `65`; fx avg `0.0` n `5`; index avg `0.0046` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.2169` n `376`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `-0.8145` n `228`; crypto_major avg `-0.5593` n `8`; equity avg `-0.0468` n `65`; fx avg `0.0002` n `5`; index avg `0.0372` n `23`; metal avg `-0.0024` n `18`; unknown avg `-0.3115` n `376`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `-1.1338` n `228`; crypto_major avg `-0.6255` n `8`; equity avg `0.0896` n `65`; fx avg `0.0002` n `5`; index avg `0.1411` n `23`; metal avg `0.0804` n `18`; unknown avg `-0.5241` n `376`
- 24h: commodity avg `0.5465` n `12`; crypto_alt avg `-1.8774` n `228`; crypto_major avg `-0.731` n `8`; equity avg `0.6304` n `65`; fx avg `-0.0083` n `5`; index avg `0.4082` n `23`; metal avg `0.2294` n `18`; unknown avg `-0.599` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
