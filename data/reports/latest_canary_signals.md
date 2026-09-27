# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T16:07:33.508607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.3502` n `234`; crypto_major avg `0.254` n `8`; equity avg `0.0576` n `141`; fx avg `0.0061` n `6`; index avg `-0.0012` n `26`; metal avg `0.0018` n `20`; unknown avg `0.2861` n `954`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `0.4855` n `234`; crypto_major avg `0.2601` n `8`; equity avg `0.0843` n `141`; fx avg `0.0073` n `6`; index avg `0.0151` n `26`; metal avg `0.0049` n `20`; unknown avg `4.9977` n `954`
- 4h: commodity avg `-0.1651` n `12`; crypto_alt avg `-1.029` n `234`; crypto_major avg `-0.9813` n `8`; equity avg `-0.0338` n `141`; fx avg `0.0165` n `6`; index avg `-0.001` n `26`; metal avg `-0.0082` n `20`; unknown avg `6.1185` n `954`
- 24h: commodity avg `-0.1073` n `12`; crypto_alt avg `-1.189` n `234`; crypto_major avg `-0.3702` n `8`; equity avg `0.2295` n `141`; fx avg `-0.0127` n `6`; index avg `0.0148` n `26`; metal avg `-0.0112` n `20`; unknown avg `122.5807` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
