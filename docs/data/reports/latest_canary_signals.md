# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T03:07:30.038103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `13`; crypto_alt avg `0.0532` n `239`; crypto_major avg `0.188` n `8`; equity avg `-0.0123` n `165`; fx avg `0.0052` n `6`; index avg `-0.0021` n `27`; metal avg `-0.2438` n `20`; unknown avg `57.5879` n `1252`
- 1h: commodity avg `0.004` n `13`; crypto_alt avg `0.0466` n `239`; crypto_major avg `0.57` n `8`; equity avg `0.0023` n `165`; fx avg `0.0146` n `6`; index avg `0.0028` n `27`; metal avg `-0.116` n `20`; unknown avg `80.6795` n `1258`
- 4h: commodity avg `-0.0921` n `13`; crypto_alt avg `-1.3696` n `239`; crypto_major avg `-0.8535` n `8`; equity avg `-1.3689` n `165`; fx avg `0.0362` n `6`; index avg `-0.1379` n `27`; metal avg `-0.8448` n `20`; unknown avg `23.9836` n `1248`
- 24h: commodity avg `-0.0238` n `13`; crypto_alt avg `-2.055` n `239`; crypto_major avg `-0.8958` n `8`; equity avg `-5.2271` n `165`; fx avg `0.0492` n `6`; index avg `-0.3694` n `27`; metal avg `-1.4541` n `20`; unknown avg `22.0791` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
