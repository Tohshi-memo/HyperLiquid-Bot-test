# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T18:07:32.190733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.0404` n `230`; crypto_major avg `0.0366` n `8`; equity avg `-0.0545` n `113`; fx avg `-0.0041` n `6`; index avg `0.0027` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0396` n `785`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `0.2093` n `230`; crypto_major avg `0.2478` n `8`; equity avg `-0.069` n `113`; fx avg `0.0084` n `6`; index avg `-0.0094` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0481` n `785`
- 4h: commodity avg `0.2202` n `12`; crypto_alt avg `-0.4443` n `230`; crypto_major avg `-0.513` n `8`; equity avg `-0.5125` n `113`; fx avg `0.003` n `6`; index avg `-0.0714` n `25`; metal avg `0.2821` n `20`; unknown avg `0.0669` n `784`
- 24h: commodity avg `1.2655` n `12`; crypto_alt avg `-0.793` n `230`; crypto_major avg `-1.3007` n `8`; equity avg `-1.3512` n `113`; fx avg `0.2512` n `6`; index avg `-0.0746` n `25`; metal avg `0.0025` n `20`; unknown avg `103.3635` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
