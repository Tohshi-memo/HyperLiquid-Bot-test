# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T01:22:28.700828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.146` n `234`; crypto_major avg `-0.126` n `8`; equity avg `0.2576` n `141`; fx avg `-0.0227` n `6`; index avg `0.0569` n `26`; metal avg `0.078` n `20`; unknown avg `1.1959` n `946`
- 1h: commodity avg `-0.0601` n `12`; crypto_alt avg `0.027` n `234`; crypto_major avg `-0.0699` n `8`; equity avg `0.263` n `141`; fx avg `-0.052` n `6`; index avg `0.0533` n `26`; metal avg `0.1262` n `20`; unknown avg `1.3834` n `944`
- 4h: commodity avg `-0.3685` n `12`; crypto_alt avg `0.0057` n `234`; crypto_major avg `-0.0727` n `8`; equity avg `0.3866` n `141`; fx avg `-0.0462` n `6`; index avg `0.0678` n `26`; metal avg `0.0933` n `20`; unknown avg `6.3058` n `898`
- 24h: commodity avg `0.5542` n `12`; crypto_alt avg `4.2089` n `234`; crypto_major avg `1.2279` n `8`; equity avg `0.2828` n `141`; fx avg `-0.0248` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0012` n `20`; unknown avg `24.3298` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
