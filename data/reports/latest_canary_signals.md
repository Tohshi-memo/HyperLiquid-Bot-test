# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T00:07:23.989592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.1086` n `234`; crypto_major avg `0.0289` n `8`; equity avg `0.1437` n `140`; fx avg `-0.0479` n `6`; index avg `0.0284` n `26`; metal avg `0.0598` n `20`; unknown avg `0.0394` n `936`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.2675` n `234`; crypto_major avg `-0.7977` n `8`; equity avg `0.2161` n `140`; fx avg `-0.0538` n `6`; index avg `0.0254` n `26`; metal avg `0.0898` n `20`; unknown avg `0.4663` n `936`
- 4h: commodity avg `0.0511` n `12`; crypto_alt avg `0.5212` n `234`; crypto_major avg `0.3079` n `8`; equity avg `0.4898` n `140`; fx avg `-0.0648` n `6`; index avg `0.0631` n `26`; metal avg `0.207` n `20`; unknown avg `-0.044` n `882`
- 24h: commodity avg `-0.6378` n `12`; crypto_alt avg `3.6532` n `234`; crypto_major avg `5.0412` n `8`; equity avg `2.6537` n `140`; fx avg `-0.1745` n `6`; index avg `0.5317` n `26`; metal avg `0.1865` n `20`; unknown avg `7.4883` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
