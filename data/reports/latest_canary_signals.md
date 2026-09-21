# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T22:37:24.935241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.0796` n `234`; crypto_major avg `-0.0047` n `8`; equity avg `0.0509` n `140`; fx avg `0.0024` n `6`; index avg `0.0206` n `26`; metal avg `0.009` n `20`; unknown avg `0.0735` n `944`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `-0.121` n `234`; crypto_major avg `0.0705` n `8`; equity avg `0.1076` n `140`; fx avg `-0.003` n `6`; index avg `0.0561` n `26`; metal avg `0.0524` n `20`; unknown avg `-0.0173` n `942`
- 4h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.8645` n `234`; crypto_major avg `1.4299` n `8`; equity avg `0.1751` n `140`; fx avg `-0.0118` n `6`; index avg `0.0323` n `26`; metal avg `0.0391` n `20`; unknown avg `-0.3017` n `852`
- 24h: commodity avg `-0.7678` n `12`; crypto_alt avg `3.5588` n `234`; crypto_major avg `6.2129` n `8`; equity avg `2.7028` n `140`; fx avg `-0.1355` n `6`; index avg `0.5711` n `26`; metal avg `0.0125` n `20`; unknown avg `7.8257` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
