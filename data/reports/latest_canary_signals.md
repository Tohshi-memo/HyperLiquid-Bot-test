# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T17:52:30.608299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `-0.138` n `235`; crypto_major avg `-0.0417` n `8`; equity avg `0.003` n `150`; fx avg `0.0006` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.7201` n `1093`
- 1h: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.1987` n `235`; crypto_major avg `-0.0061` n `8`; equity avg `0.0002` n `150`; fx avg `-0.005` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0069` n `20`; unknown avg `0.2152` n `1075`
- 4h: commodity avg `-0.0075` n `13`; crypto_alt avg `0.649` n `235`; crypto_major avg `0.2809` n `8`; equity avg `0.0551` n `150`; fx avg `-0.0048` n `6`; index avg `0.008` n `26`; metal avg `-0.024` n `20`; unknown avg `-0.0296` n `1061`
- 24h: commodity avg `-0.4088` n `13`; crypto_alt avg `2.3095` n `235`; crypto_major avg `0.7867` n `8`; equity avg `0.1231` n `150`; fx avg `0.0031` n `6`; index avg `0.0326` n `26`; metal avg `-0.0182` n `20`; unknown avg `0.3036` n `952`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
