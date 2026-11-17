# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T16:07:39.548141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.147` n `13`; crypto_alt avg `1.1768` n `239`; crypto_major avg `1.1429` n `8`; equity avg `1.5293` n `163`; fx avg `0.0079` n `6`; index avg `0.1391` n `27`; metal avg `0.0149` n `20`; unknown avg `6.6002` n `1249`
- 1h: commodity avg `0.0949` n `13`; crypto_alt avg `-0.5087` n `239`; crypto_major avg `-0.6519` n `8`; equity avg `-1.0388` n `163`; fx avg `0.0372` n `6`; index avg `-0.1178` n `27`; metal avg `0.0058` n `20`; unknown avg `4.1243` n `1245`
- 4h: commodity avg `0.2231` n `13`; crypto_alt avg `-0.9532` n `239`; crypto_major avg `-1.087` n `8`; equity avg `-2.2279` n `163`; fx avg `0.052` n `6`; index avg `-0.2255` n `27`; metal avg `-0.1374` n `20`; unknown avg `9.6795` n `1209`
- 24h: commodity avg `-0.1042` n `13`; crypto_alt avg `0.1294` n `239`; crypto_major avg `0.1895` n `8`; equity avg `-2.7718` n `163`; fx avg `0.0037` n `6`; index avg `-0.3805` n `27`; metal avg `0.0124` n `20`; unknown avg `12.5071` n `1096`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
