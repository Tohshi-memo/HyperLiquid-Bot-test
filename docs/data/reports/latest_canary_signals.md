# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T09:37:29.740977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `-0.1299` n `8`; equity avg `0.0002` n `108`; fx avg `0.007` n `6`; index avg `0.0059` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.1088` n `782`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `-0.2602` n `230`; crypto_major avg `-0.319` n `8`; equity avg `-0.1722` n `108`; fx avg `-0.0077` n `6`; index avg `-0.0316` n `25`; metal avg `0.1177` n `20`; unknown avg `-0.0893` n `782`
- 4h: commodity avg `0.087` n `12`; crypto_alt avg `-0.0937` n `230`; crypto_major avg `-0.4918` n `8`; equity avg `-0.3399` n `108`; fx avg `0.1075` n `6`; index avg `-0.0429` n `25`; metal avg `0.2293` n `20`; unknown avg `-0.05` n `750`
- 24h: commodity avg `-0.2226` n `12`; crypto_alt avg `-0.0366` n `230`; crypto_major avg `-0.5769` n `8`; equity avg `-1.7216` n `108`; fx avg `0.0092` n `6`; index avg `-0.346` n `25`; metal avg `0.5324` n `20`; unknown avg `0.0848` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
