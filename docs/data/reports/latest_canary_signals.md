# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T21:22:28.809482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `0.0704` n `234`; crypto_major avg `-0.2511` n `8`; equity avg `0.0097` n `140`; fx avg `-0.0074` n `6`; index avg `-0.0049` n `26`; metal avg `0.0014` n `20`; unknown avg `0.478` n `942`
- 1h: commodity avg `-0.0035` n `12`; crypto_alt avg `0.2999` n `234`; crypto_major avg `-0.2266` n `8`; equity avg `-0.0072` n `140`; fx avg `0.0377` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0533` n `20`; unknown avg `0.1886` n `932`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `1.3345` n `234`; crypto_major avg `0.733` n `8`; equity avg `0.7732` n `140`; fx avg `0.0653` n `6`; index avg `0.1471` n `26`; metal avg `-0.0771` n `20`; unknown avg `6.3917` n `878`
- 24h: commodity avg `-0.089` n `12`; crypto_alt avg `7.2131` n `234`; crypto_major avg `6.9402` n `8`; equity avg `1.3021` n `140`; fx avg `0.2665` n `6`; index avg `0.0393` n `26`; metal avg `0.3634` n `20`; unknown avg `8.7716` n `727`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
