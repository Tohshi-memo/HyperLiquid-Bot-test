# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T02:07:29.362356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.0221` n `234`; crypto_major avg `0.0366` n `8`; equity avg `-0.003` n `141`; fx avg `0.006` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.0097` n `959`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.4462` n `234`; crypto_major avg `0.3407` n `8`; equity avg `0.0238` n `141`; fx avg `0.0054` n `6`; index avg `-0.0011` n `26`; metal avg `0.0012` n `20`; unknown avg `0.085` n `959`
- 4h: commodity avg `-0.104` n `12`; crypto_alt avg `0.2021` n `234`; crypto_major avg `0.2329` n `8`; equity avg `0.069` n `141`; fx avg `0.007` n `6`; index avg `0.0028` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.9419` n `951`
- 24h: commodity avg `-0.0746` n `12`; crypto_alt avg `0.8767` n `234`; crypto_major avg `-0.5644` n `8`; equity avg `0.1891` n `141`; fx avg `0.0234` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0114` n `20`; unknown avg `4.277` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
