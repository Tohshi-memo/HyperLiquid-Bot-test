# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T00:37:32.974830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `0.1889` n `234`; crypto_major avg `0.3094` n `8`; equity avg `-0.0113` n `140`; fx avg `0.0` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0112` n `20`; unknown avg `-0.1661` n `942`
- 1h: commodity avg `0.0809` n `12`; crypto_alt avg `0.5103` n `234`; crypto_major avg `0.5357` n `8`; equity avg `0.0511` n `140`; fx avg `-0.0131` n `6`; index avg `-0.0123` n `26`; metal avg `-0.01` n `20`; unknown avg `0.1437` n `934`
- 4h: commodity avg `0.176` n `12`; crypto_alt avg `0.7119` n `234`; crypto_major avg `0.4429` n `8`; equity avg `0.0601` n `140`; fx avg `0.0159` n `6`; index avg `-0.0273` n `26`; metal avg `-0.0312` n `20`; unknown avg `10.2244` n `908`
- 24h: commodity avg `0.1486` n `12`; crypto_alt avg `6.9068` n `234`; crypto_major avg `6.9479` n `8`; equity avg `1.4666` n `140`; fx avg `0.1684` n `6`; index avg `0.099` n `26`; metal avg `0.236` n `20`; unknown avg `4.0379` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
