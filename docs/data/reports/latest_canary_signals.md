# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T06:52:27.642634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.145` n `236`; crypto_major avg `-0.2423` n `8`; equity avg `-0.175` n `151`; fx avg `0.0017` n `6`; index avg `-0.0194` n `26`; metal avg `-0.0097` n `20`; unknown avg `-0.0021` n `1136`
- 1h: commodity avg `-0.0124` n `13`; crypto_alt avg `0.4572` n `236`; crypto_major avg `0.373` n `8`; equity avg `-0.0723` n `151`; fx avg `-0.0821` n `6`; index avg `0.0218` n `26`; metal avg `-0.0612` n `20`; unknown avg `0.2104` n `1108`
- 4h: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.5879` n `236`; crypto_major avg `-0.3298` n `8`; equity avg `-0.4413` n `151`; fx avg `-0.1246` n `6`; index avg `-0.0133` n `26`; metal avg `-0.1196` n `20`; unknown avg `0.8563` n `1102`
- 24h: commodity avg `-0.3391` n `13`; crypto_alt avg `-5.3769` n `236`; crypto_major avg `-3.8032` n `8`; equity avg `-5.8521` n `151`; fx avg `0.01` n `6`; index avg `-0.99` n `26`; metal avg `-0.7163` n `20`; unknown avg `1393.1271` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.093`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
