# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T06:37:23.946263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `13`; crypto_alt avg `-0.1525` n `239`; crypto_major avg `-0.1369` n `8`; equity avg `-0.1195` n `161`; fx avg `0.0278` n `6`; index avg `-0.0394` n `27`; metal avg `-0.0489` n `20`; unknown avg `0.3032` n `1258`
- 1h: commodity avg `0.1774` n `13`; crypto_alt avg `-0.1992` n `239`; crypto_major avg `-0.1017` n `8`; equity avg `0.098` n `161`; fx avg `0.0199` n `6`; index avg `-0.0178` n `27`; metal avg `-0.0288` n `20`; unknown avg `42.8499` n `1224`
- 4h: commodity avg `0.0204` n `13`; crypto_alt avg `-0.6712` n `239`; crypto_major avg `-0.6891` n `8`; equity avg `-1.4315` n `161`; fx avg `-0.0655` n `6`; index avg `-0.1594` n `27`; metal avg `-0.052` n `20`; unknown avg `0.3116` n `1204`
- 24h: commodity avg `0.1156` n `13`; crypto_alt avg `-1.5694` n `239`; crypto_major avg `-0.8631` n `8`; equity avg `-0.7971` n `161`; fx avg `-0.1513` n `6`; index avg `-0.1252` n `27`; metal avg `-0.6136` n `20`; unknown avg `-0.3832` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
