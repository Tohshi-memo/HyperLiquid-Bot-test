# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T09:37:48.534359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1334` n `13`; crypto_alt avg `0.0533` n `239`; crypto_major avg `0.0523` n `8`; equity avg `-0.0424` n `164`; fx avg `-0.0077` n `6`; index avg `-0.0123` n `27`; metal avg `0.0541` n `20`; unknown avg `0.8317` n `1266`
- 1h: commodity avg `-0.111` n `13`; crypto_alt avg `0.2982` n `239`; crypto_major avg `0.2344` n `8`; equity avg `-0.0852` n `164`; fx avg `0.0183` n `6`; index avg `-0.023` n `27`; metal avg `0.0114` n `20`; unknown avg `261.5134` n `1262`
- 4h: commodity avg `-0.1796` n `13`; crypto_alt avg `0.6775` n `239`; crypto_major avg `0.568` n `8`; equity avg `1.0765` n `164`; fx avg `0.0914` n `6`; index avg `0.1567` n `27`; metal avg `-0.0482` n `20`; unknown avg `277.2763` n `1202`
- 24h: commodity avg `0.0422` n `13`; crypto_alt avg `0.144` n `239`; crypto_major avg `-0.5658` n `8`; equity avg `-0.1103` n `164`; fx avg `0.052` n `6`; index avg `0.1068` n `27`; metal avg `-0.1995` n `20`; unknown avg `3.4644` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
