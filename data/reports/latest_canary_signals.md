# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T08:52:31.394894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1724` n `234`; crypto_major avg `0.0008` n `8`; equity avg `-0.0053` n `140`; fx avg `0.004` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.7697` n `942`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `0.7999` n `234`; crypto_major avg `0.3627` n `8`; equity avg `0.0185` n `140`; fx avg `-0.0127` n `6`; index avg `0.0154` n `26`; metal avg `-0.0045` n `20`; unknown avg `2.0141` n `934`
- 4h: commodity avg `0.0049` n `12`; crypto_alt avg `0.654` n `234`; crypto_major avg `0.344` n `8`; equity avg `0.0067` n `140`; fx avg `-0.0017` n `6`; index avg `-0.014` n `26`; metal avg `-0.0075` n `20`; unknown avg `2.0694` n `898`
- 24h: commodity avg `0.2534` n `12`; crypto_alt avg `3.3783` n `234`; crypto_major avg `4.034` n `8`; equity avg `0.0474` n `140`; fx avg `-0.039` n `6`; index avg `-0.0662` n `26`; metal avg `-0.2406` n `20`; unknown avg `2.8372` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
