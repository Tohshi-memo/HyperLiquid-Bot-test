# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T21:07:32.057763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `13`; crypto_alt avg `-0.2184` n `239`; crypto_major avg `-0.1614` n `8`; equity avg `0.1202` n `161`; fx avg `0.0014` n `6`; index avg `-0.0046` n `27`; metal avg `-0.0286` n `20`; unknown avg `3.808` n `1220`
- 1h: commodity avg `0.0608` n `13`; crypto_alt avg `-0.0148` n `239`; crypto_major avg `0.1437` n `8`; equity avg `-0.1168` n `161`; fx avg `-0.0048` n `6`; index avg `-0.0288` n `27`; metal avg `-0.0454` n `20`; unknown avg `3.9239` n `1216`
- 4h: commodity avg `-0.3039` n `13`; crypto_alt avg `-0.8942` n `239`; crypto_major avg `-0.1708` n `8`; equity avg `-0.7` n `161`; fx avg `0.0118` n `6`; index avg `-0.0475` n `27`; metal avg `-0.2038` n `20`; unknown avg `4.1019` n `1208`
- 24h: commodity avg `0.2066` n `13`; crypto_alt avg `0.3561` n `239`; crypto_major avg `0.8468` n `8`; equity avg `4.4065` n `161`; fx avg `-0.1431` n `6`; index avg `0.4322` n `27`; metal avg `-0.0785` n `20`; unknown avg `6.0677` n `1141`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `670`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1195`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `670`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1054`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1012`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0956`, n `670`, weak_sample_signal
