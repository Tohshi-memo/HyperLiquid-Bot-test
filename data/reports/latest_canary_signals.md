# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:37:26.519460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.003` n `230`; crypto_major avg `-0.0194` n `8`; equity avg `0.0199` n `113`; fx avg `0.0024` n `6`; index avg `-0.0058` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0438` n `785`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.0065` n `230`; crypto_major avg `0.0112` n `8`; equity avg `-0.1604` n `113`; fx avg `0.0097` n `6`; index avg `-0.0174` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.1404` n `785`
- 4h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.5021` n `230`; crypto_major avg `-0.3711` n `8`; equity avg `-0.6257` n `113`; fx avg `-0.0007` n `6`; index avg `-0.0622` n `25`; metal avg `0.0156` n `20`; unknown avg `2.8811` n `785`
- 24h: commodity avg `0.7751` n `12`; crypto_alt avg `-0.3129` n `230`; crypto_major avg `-0.4649` n `8`; equity avg `-1.8091` n `113`; fx avg `0.2752` n `6`; index avg `-0.0813` n `25`; metal avg `0.3719` n `20`; unknown avg `103.664` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
