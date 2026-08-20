# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T21:37:33.886161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1369` n `230`; crypto_major avg `0.2177` n `8`; equity avg `0.1193` n `121`; fx avg `-0.0094` n `6`; index avg `-0.0014` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0377` n `793`
- 1h: commodity avg `-0.042` n `12`; crypto_alt avg `0.328` n `230`; crypto_major avg `0.451` n `8`; equity avg `0.1401` n `121`; fx avg `-0.0139` n `6`; index avg `0.0041` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0645` n `792`
- 4h: commodity avg `0.0282` n `12`; crypto_alt avg `-0.2109` n `230`; crypto_major avg `-0.9857` n `8`; equity avg `0.4978` n `121`; fx avg `-0.0169` n `6`; index avg `-0.0068` n `25`; metal avg `0.0469` n `20`; unknown avg `-0.2259` n `792`
- 24h: commodity avg `0.2766` n `12`; crypto_alt avg `3.7449` n `230`; crypto_major avg `4.2956` n `8`; equity avg `-0.7919` n `121`; fx avg `0.208` n `6`; index avg `-0.0878` n `25`; metal avg `0.0674` n `20`; unknown avg `2.7041` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2204`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
