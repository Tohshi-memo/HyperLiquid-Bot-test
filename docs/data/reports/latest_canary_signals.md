# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T16:37:26.208655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0348` n `238`; crypto_major avg `0.025` n `8`; equity avg `-0.0353` n `156`; fx avg `0.0065` n `6`; index avg `-0.0003` n `27`; metal avg `0.0018` n `20`; unknown avg `0.0559` n `1262`
- 1h: commodity avg `-0.0546` n `13`; crypto_alt avg `0.0762` n `238`; crypto_major avg `-0.0185` n `8`; equity avg `-0.0438` n `156`; fx avg `-0.0071` n `6`; index avg `-0.0006` n `27`; metal avg `0.0052` n `20`; unknown avg `2.3616` n `1240`
- 4h: commodity avg `-0.1425` n `13`; crypto_alt avg `0.6714` n `238`; crypto_major avg `-0.087` n `8`; equity avg `0.0201` n `156`; fx avg `-0.0093` n `6`; index avg `-0.006` n `27`; metal avg `0.0228` n `20`; unknown avg `3.5585` n `1236`
- 24h: commodity avg `-0.3278` n `13`; crypto_alt avg `1.1451` n `238`; crypto_major avg `-0.2542` n `8`; equity avg `0.2525` n `156`; fx avg `-0.0128` n `6`; index avg `-0.0584` n `27`; metal avg `-0.0276` n `20`; unknown avg `1.4389` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
