# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T13:07:33.208720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.105` n `13`; crypto_alt avg `0.3452` n `235`; crypto_major avg `0.2569` n `8`; equity avg `0.182` n `150`; fx avg `0.0185` n `6`; index avg `0.0457` n `26`; metal avg `0.0286` n `20`; unknown avg `1.2066` n `1076`
- 1h: commodity avg `0.0858` n `13`; crypto_alt avg `-0.073` n `235`; crypto_major avg `-0.2542` n `8`; equity avg `0.0053` n `150`; fx avg `-0.005` n `6`; index avg `-0.0042` n `26`; metal avg `-0.057` n `20`; unknown avg `1.6229` n `1076`
- 4h: commodity avg `0.0883` n `13`; crypto_alt avg `-0.3701` n `235`; crypto_major avg `-0.0007` n `8`; equity avg `0.0146` n `150`; fx avg `-0.0422` n `6`; index avg `-0.023` n `26`; metal avg `-0.0583` n `20`; unknown avg `2.1687` n `1070`
- 24h: commodity avg `-0.4047` n `13`; crypto_alt avg `-0.6858` n `235`; crypto_major avg `-0.7343` n `8`; equity avg `-0.1994` n `150`; fx avg `0.0213` n `6`; index avg `0.0314` n `26`; metal avg `0.4836` n `20`; unknown avg `7.5661` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
