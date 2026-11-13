# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T11:37:27.952592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `13`; crypto_alt avg `-0.0948` n `239`; crypto_major avg `-0.1675` n `8`; equity avg `-0.1846` n `162`; fx avg `0.018` n `6`; index avg `-0.0162` n `27`; metal avg `0.0031` n `20`; unknown avg `33.5666` n `1262`
- 1h: commodity avg `0.0834` n `13`; crypto_alt avg `0.142` n `239`; crypto_major avg `0.1121` n `8`; equity avg `0.2062` n `162`; fx avg `0.0232` n `6`; index avg `0.0157` n `27`; metal avg `0.0091` n `20`; unknown avg `39.5884` n `1258`
- 4h: commodity avg `-0.0226` n `13`; crypto_alt avg `-0.2626` n `239`; crypto_major avg `0.4535` n `8`; equity avg `0.325` n `162`; fx avg `-0.0033` n `6`; index avg `0.0409` n `27`; metal avg `-0.0321` n `20`; unknown avg `48.6552` n `1148`
- 24h: commodity avg `0.6663` n `13`; crypto_alt avg `-0.3103` n `239`; crypto_major avg `-1.8904` n `8`; equity avg `-0.6781` n `162`; fx avg `-0.0281` n `6`; index avg `0.0562` n `27`; metal avg `-0.3751` n `20`; unknown avg `4.0297` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
