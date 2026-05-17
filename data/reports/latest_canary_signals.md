# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T20:52:15.364355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `0.0072` n `228`; crypto_major avg `0.1135` n `8`; equity avg `0.0568` n `65`; fx avg `-0.0052` n `5`; index avg `0.0006` n `23`; metal avg `-0.0066` n `18`; unknown avg `-0.074` n `384`
- 1h: commodity avg `-0.1049` n `12`; crypto_alt avg `-0.1037` n `228`; crypto_major avg `-0.1335` n `8`; equity avg `0.0748` n `65`; fx avg `-0.0028` n `5`; index avg `0.0549` n `23`; metal avg `0.0026` n `18`; unknown avg `-0.3423` n `384`
- 4h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.2048` n `228`; crypto_major avg `1.1217` n `8`; equity avg `0.308` n `65`; fx avg `0.0075` n `5`; index avg `0.1287` n `23`; metal avg `-0.1303` n `18`; unknown avg `0.2855` n `384`
- 24h: commodity avg `1.7443` n `12`; crypto_alt avg `-9.172` n `228`; crypto_major avg `-1.3633` n `8`; equity avg `-2.2225` n `65`; fx avg `-0.1577` n `5`; index avg `-1.4853` n `23`; metal avg `-5.9485` n `18`; unknown avg `550.3913` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
