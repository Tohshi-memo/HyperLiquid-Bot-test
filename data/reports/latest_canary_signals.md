# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T21:22:39.683382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `12`; crypto_alt avg `0.4235` n `234`; crypto_major avg `0.2331` n `8`; equity avg `0.022` n `141`; fx avg `-0.008` n `6`; index avg `0.0015` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.6662` n `946`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `0.2034` n `234`; crypto_major avg `0.033` n `8`; equity avg `0.1536` n `141`; fx avg `-0.0137` n `6`; index avg `0.0258` n `26`; metal avg `0.0301` n `20`; unknown avg `2.1558` n `938`
- 4h: commodity avg `-0.1626` n `12`; crypto_alt avg `0.3358` n `234`; crypto_major avg `0.0935` n `8`; equity avg `-0.1065` n `141`; fx avg `-0.0137` n `6`; index avg `-0.0419` n `26`; metal avg `0.0367` n `20`; unknown avg `6.2544` n `869`
- 24h: commodity avg `0.7462` n `12`; crypto_alt avg `4.5188` n `234`; crypto_major avg `1.6846` n `8`; equity avg `-0.2441` n `141`; fx avg `0.0277` n `6`; index avg `-0.1111` n `26`; metal avg `-0.1303` n `20`; unknown avg `18.5709` n `855`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
