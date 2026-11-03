# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T13:22:28.732745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1459` n `13`; crypto_alt avg `-0.3013` n `239`; crypto_major avg `-0.1859` n `8`; equity avg `-0.0444` n `157`; fx avg `0.0082` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0598` n `20`; unknown avg `0.0895` n `1262`
- 1h: commodity avg `-0.1782` n `13`; crypto_alt avg `-0.2239` n `239`; crypto_major avg `-0.308` n `8`; equity avg `0.196` n `157`; fx avg `-0.0076` n `6`; index avg `0.0241` n `27`; metal avg `0.1365` n `20`; unknown avg `2.3622` n `1256`
- 4h: commodity avg `-0.2633` n `13`; crypto_alt avg `1.003` n `239`; crypto_major avg `0.7062` n `8`; equity avg `0.5311` n `157`; fx avg `0.0148` n `6`; index avg `0.0509` n `27`; metal avg `0.2714` n `20`; unknown avg `1.2997` n `1222`
- 24h: commodity avg `-0.5657` n `13`; crypto_alt avg `-0.5441` n `239`; crypto_major avg `-0.0812` n `8`; equity avg `-2.4297` n `157`; fx avg `0.0058` n `6`; index avg `-0.1538` n `27`; metal avg `-0.1546` n `20`; unknown avg `-0.0102` n `1022`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
