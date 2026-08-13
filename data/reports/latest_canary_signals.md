# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T07:22:31.131678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `0.0013` n `113`; fx avg `0.004` n `6`; index avg `-0.0` n `25`; metal avg `-0.0595` n `20`; unknown avg `0.0203` n `787`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0665` n `230`; crypto_major avg `0.0872` n `8`; equity avg `-0.4342` n `113`; fx avg `0.0538` n `6`; index avg `-0.023` n `25`; metal avg `-0.0999` n `20`; unknown avg `-0.0255` n `787`
- 4h: commodity avg `0.1213` n `12`; crypto_alt avg `0.2461` n `230`; crypto_major avg `0.5374` n `8`; equity avg `-0.5693` n `113`; fx avg `0.0683` n `6`; index avg `-0.0633` n `25`; metal avg `-0.2831` n `20`; unknown avg `0.0696` n `754`
- 24h: commodity avg `-0.1187` n `12`; crypto_alt avg `-0.5561` n `230`; crypto_major avg `0.4295` n `8`; equity avg `1.7784` n `113`; fx avg `-0.001` n `6`; index avg `0.2358` n `25`; metal avg `-0.4169` n `20`; unknown avg `0.1124` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2461`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
