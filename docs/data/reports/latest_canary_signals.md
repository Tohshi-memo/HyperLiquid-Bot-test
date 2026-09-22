# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T09:37:33.912936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0783` n `12`; crypto_alt avg `0.2504` n `234`; crypto_major avg `0.1386` n `8`; equity avg `0.0336` n `140`; fx avg `-0.0056` n `6`; index avg `0.0059` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.0737` n `944`
- 1h: commodity avg `-0.2908` n `12`; crypto_alt avg `-0.1164` n `234`; crypto_major avg `0.1711` n `8`; equity avg `0.4612` n `140`; fx avg `-0.0361` n `6`; index avg `0.0763` n `26`; metal avg `0.1062` n `20`; unknown avg `0.4092` n `942`
- 4h: commodity avg `-0.4233` n `12`; crypto_alt avg `0.8963` n `234`; crypto_major avg `0.7555` n `8`; equity avg `0.0876` n `140`; fx avg `-0.0846` n `6`; index avg `-0.0092` n `26`; metal avg `0.0161` n `20`; unknown avg `9.8092` n `908`
- 24h: commodity avg `-0.5673` n `12`; crypto_alt avg `0.7411` n `234`; crypto_major avg `1.2012` n `8`; equity avg `0.6467` n `140`; fx avg `-0.2673` n `6`; index avg `0.2247` n `26`; metal avg `-0.1665` n `20`; unknown avg `1120.3424` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
