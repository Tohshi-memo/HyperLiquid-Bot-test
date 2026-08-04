# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T10:52:31.575554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2265` n `12`; crypto_alt avg `0.3229` n `230`; crypto_major avg `0.4482` n `8`; equity avg `0.1941` n `107`; fx avg `0.0025` n `6`; index avg `0.0315` n `25`; metal avg `0.0863` n `20`; unknown avg `0.1001` n `781`
- 1h: commodity avg `-0.3843` n `12`; crypto_alt avg `0.213` n `230`; crypto_major avg `0.4374` n `8`; equity avg `0.5776` n `107`; fx avg `-0.0218` n `6`; index avg `0.0647` n `25`; metal avg `0.1291` n `20`; unknown avg `0.0853` n `781`
- 4h: commodity avg `-0.1101` n `12`; crypto_alt avg `0.1995` n `230`; crypto_major avg `0.4486` n `8`; equity avg `0.552` n `107`; fx avg `-0.0092` n `6`; index avg `0.041` n `25`; metal avg `0.1446` n `20`; unknown avg `0.9613` n `781`
- 24h: commodity avg `0.1938` n `12`; crypto_alt avg `1.1539` n `230`; crypto_major avg `1.5087` n `8`; equity avg `4.3906` n `107`; fx avg `0.0928` n `6`; index avg `0.4335` n `25`; metal avg `0.3654` n `20`; unknown avg `1.0994` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
