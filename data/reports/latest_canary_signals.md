# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T16:22:43.182498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5951` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `0.0552` n `8`; equity avg `0.1301` n `107`; fx avg `-0.0095` n `6`; index avg `0.0073` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0172` n `782`
- 1h: commodity avg `-0.1396` n `12`; crypto_alt avg `0.2295` n `230`; crypto_major avg `0.1015` n `8`; equity avg `0.4452` n `107`; fx avg `0.0061` n `6`; index avg `0.0669` n `25`; metal avg `0.1011` n `20`; unknown avg `-0.081` n `782`
- 4h: commodity avg `-0.5466` n `12`; crypto_alt avg `-0.0725` n `230`; crypto_major avg `-0.0157` n `8`; equity avg `1.5794` n `107`; fx avg `0.0153` n `6`; index avg `0.3569` n `25`; metal avg `0.2463` n `20`; unknown avg `-0.3073` n `781`
- 24h: commodity avg `-1.1045` n `12`; crypto_alt avg `-0.2133` n `230`; crypto_major avg `0.066` n `8`; equity avg `4.179` n `107`; fx avg `0.0691` n `6`; index avg `0.7753` n `25`; metal avg `1.1541` n `20`; unknown avg `0.4168` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
