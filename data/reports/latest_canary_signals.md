# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T07:22:28.016933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.052` n `13`; crypto_alt avg `0.325` n `236`; crypto_major avg `0.269` n `8`; equity avg `0.014` n `151`; fx avg `0.04` n `6`; index avg `0.0141` n `26`; metal avg `0.0299` n `20`; unknown avg `0.1309` n `1136`
- 1h: commodity avg `-0.0508` n `13`; crypto_alt avg `0.1927` n `236`; crypto_major avg `0.3186` n `8`; equity avg `-0.2633` n `151`; fx avg `-0.0325` n `6`; index avg `-0.0438` n `26`; metal avg `0.1021` n `20`; unknown avg `0.0029` n `1134`
- 4h: commodity avg `-0.059` n `13`; crypto_alt avg `-0.5067` n `236`; crypto_major avg `0.1464` n `8`; equity avg `-0.3164` n `151`; fx avg `-0.0728` n `6`; index avg `0.0254` n `26`; metal avg `0.011` n `20`; unknown avg `1.1318` n `1102`
- 24h: commodity avg `-0.458` n `13`; crypto_alt avg `-5.341` n `236`; crypto_major avg `-3.6419` n `8`; equity avg `-5.8964` n `151`; fx avg `0.0602` n `6`; index avg `-0.9605` n `26`; metal avg `-0.5278` n `20`; unknown avg `1393.2284` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0876`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0665`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
