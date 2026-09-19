# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T01:37:27.205841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.0601` n `234`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0223` n `140`; fx avg `0.0102` n `6`; index avg `-0.0094` n `26`; metal avg `0.0055` n `20`; unknown avg `-0.0809` n `942`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `-0.8039` n `234`; crypto_major avg `-0.4403` n `8`; equity avg `-0.1293` n `140`; fx avg `-0.0025` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0306` n `20`; unknown avg `0.0227` n `940`
- 4h: commodity avg `0.1778` n `12`; crypto_alt avg `-0.4519` n `234`; crypto_major avg `-0.2384` n `8`; equity avg `-0.1142` n `140`; fx avg `-0.0109` n `6`; index avg `-0.007` n `26`; metal avg `-0.046` n `20`; unknown avg `16.17` n `916`
- 24h: commodity avg `0.1462` n `12`; crypto_alt avg `5.3104` n `234`; crypto_major avg `5.8106` n `8`; equity avg `1.4254` n `140`; fx avg `0.1575` n `6`; index avg `0.1505` n `26`; metal avg `0.1818` n `20`; unknown avg `4.0603` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
