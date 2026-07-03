# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T23:22:28.017609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.008` n `229`; crypto_major avg `0.0986` n `8`; equity avg `0.0421` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0052` n `25`; metal avg `0.0061` n `20`; unknown avg `0.6313` n `765`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.1392` n `229`; crypto_major avg `-0.038` n `8`; equity avg `0.0071` n `88`; fx avg `-0.001` n `6`; index avg `0.0045` n `25`; metal avg `0.0259` n `20`; unknown avg `0.1426` n `765`
- 4h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.2436` n `229`; crypto_major avg `0.2488` n `8`; equity avg `-0.1097` n `88`; fx avg `-0.0183` n `6`; index avg `-0.0356` n `25`; metal avg `0.0256` n `20`; unknown avg `0.075` n `765`
- 24h: commodity avg `0.1493` n `12`; crypto_alt avg `3.0573` n `229`; crypto_major avg `3.1894` n `8`; equity avg `1.8646` n `88`; fx avg `-0.0633` n `6`; index avg `0.4278` n `25`; metal avg `0.5383` n `20`; unknown avg `5.7313` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
