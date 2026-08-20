# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T20:37:34.259348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1119` n `230`; crypto_major avg `0.2364` n `8`; equity avg `-0.0023` n `121`; fx avg `0.0064` n `6`; index avg `0.0106` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.0318` n `792`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.3161` n `230`; crypto_major avg `0.381` n `8`; equity avg `0.0725` n `121`; fx avg `-0.0111` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.2103` n `792`
- 4h: commodity avg `0.1077` n `12`; crypto_alt avg `0.1256` n `230`; crypto_major avg `-0.4073` n `8`; equity avg `0.297` n `121`; fx avg `-0.0093` n `6`; index avg `-0.0473` n `25`; metal avg `0.0536` n `20`; unknown avg `0.9294` n `792`
- 24h: commodity avg `0.3767` n `12`; crypto_alt avg `5.2276` n `230`; crypto_major avg `7.0857` n `8`; equity avg `-0.5806` n `121`; fx avg `0.1967` n `6`; index avg `-0.0299` n `25`; metal avg `0.1143` n `20`; unknown avg `2.9737` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
