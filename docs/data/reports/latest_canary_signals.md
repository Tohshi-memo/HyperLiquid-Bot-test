# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T23:37:28.382475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.0089` n `230`; crypto_major avg `0.1779` n `8`; equity avg `0.0085` n `113`; fx avg `0.002` n `6`; index avg `0.0013` n `25`; metal avg `-0.0224` n `20`; unknown avg `0.092` n `786`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.0972` n `230`; crypto_major avg `-0.0214` n `8`; equity avg `0.0764` n `113`; fx avg `-0.0057` n `6`; index avg `0.0039` n `25`; metal avg `-0.0421` n `20`; unknown avg `-0.0362` n `786`
- 4h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.3607` n `230`; crypto_major avg `0.8065` n `8`; equity avg `0.5194` n `113`; fx avg `-0.0062` n `6`; index avg `0.0109` n `25`; metal avg `0.0018` n `20`; unknown avg `0.2805` n `785`
- 24h: commodity avg `0.1557` n `12`; crypto_alt avg `-1.1076` n `230`; crypto_major avg `0.7977` n `8`; equity avg `1.5233` n `113`; fx avg `-0.0731` n `6`; index avg `0.1373` n `25`; metal avg `-0.2409` n `20`; unknown avg `-0.1173` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2149`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
