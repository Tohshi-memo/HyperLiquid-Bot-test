# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T06:07:52.324882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2519` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0604` n `234`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0142` n `140`; fx avg `0.0175` n `6`; index avg `0.003` n `26`; metal avg `0.001` n `20`; unknown avg `0.3648` n `911`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `0.0123` n `234`; crypto_major avg `-0.1274` n `8`; equity avg `-0.0127` n `140`; fx avg `0.0118` n `6`; index avg `0.0027` n `26`; metal avg `0.0039` n `20`; unknown avg `1.4225` n `911`
- 4h: commodity avg `0.0396` n `12`; crypto_alt avg `-1.6348` n `234`; crypto_major avg `-1.3321` n `8`; equity avg `-0.4503` n `140`; fx avg `0.0061` n `6`; index avg `-0.0802` n `26`; metal avg `-0.0203` n `20`; unknown avg `1.2384` n `895`
- 24h: commodity avg `0.2446` n `12`; crypto_alt avg `0.2916` n `234`; crypto_major avg `-1.8564` n `8`; equity avg `-0.1767` n `140`; fx avg `-0.0373` n `6`; index avg `-0.0164` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.6863` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
