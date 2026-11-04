# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T06:07:29.766431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1527` n `13`; crypto_alt avg `-0.2629` n `239`; crypto_major avg `-0.2623` n `8`; equity avg `0.4709` n `158`; fx avg `0.0123` n `6`; index avg `0.0223` n `27`; metal avg `0.0493` n `20`; unknown avg `0.3368` n `1242`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `0.9138` n `239`; crypto_major avg `0.604` n `8`; equity avg `1.6331` n `158`; fx avg `0.0137` n `6`; index avg `0.1878` n `27`; metal avg `0.6351` n `20`; unknown avg `1.0676` n `1242`
- 4h: commodity avg `0.2977` n `13`; crypto_alt avg `1.1758` n `239`; crypto_major avg `0.9099` n `8`; equity avg `1.5354` n `158`; fx avg `0.0658` n `6`; index avg `0.2203` n `27`; metal avg `0.6422` n `20`; unknown avg `4.2418` n `1238`
- 24h: commodity avg `0.0226` n `13`; crypto_alt avg `2.0793` n `239`; crypto_major avg `1.3959` n `8`; equity avg `2.5529` n `158`; fx avg `0.1463` n `6`; index avg `0.1028` n `27`; metal avg `0.5733` n `20`; unknown avg `190.5929` n `1051`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
