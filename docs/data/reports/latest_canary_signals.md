# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T11:37:28.568285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0629` n `12`; crypto_alt avg `0.1966` n `232`; crypto_major avg `0.1504` n `8`; equity avg `-0.0197` n `133`; fx avg `0.0213` n `6`; index avg `0.0035` n `26`; metal avg `0.0206` n `20`; unknown avg `1.4817` n `792`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `0.5243` n `232`; crypto_major avg `0.6872` n `8`; equity avg `0.2802` n `133`; fx avg `-0.0301` n `6`; index avg `0.0535` n `26`; metal avg `0.0889` n `20`; unknown avg `1.8043` n `790`
- 4h: commodity avg `0.4052` n `12`; crypto_alt avg `0.1808` n `232`; crypto_major avg `0.1485` n `8`; equity avg `-0.1191` n `133`; fx avg `-0.0973` n `6`; index avg `-0.0208` n `26`; metal avg `0.0046` n `20`; unknown avg `0.4593` n `790`
- 24h: commodity avg `0.7454` n `12`; crypto_alt avg `2.2062` n `232`; crypto_major avg `2.0978` n `8`; equity avg `1.5044` n `133`; fx avg `-0.3704` n `6`; index avg `0.0815` n `26`; metal avg `0.6153` n `20`; unknown avg `-0.1253` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0418`, n `668`, weak_sample_signal
