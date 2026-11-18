# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T10:22:28.586068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `13`; crypto_alt avg `-0.0535` n `239`; crypto_major avg `-0.1621` n `8`; equity avg `-0.2514` n `163`; fx avg `-0.0171` n `6`; index avg `-0.025` n `27`; metal avg `-0.053` n `20`; unknown avg `1.7575` n `1264`
- 1h: commodity avg `0.0475` n `13`; crypto_alt avg `0.0053` n `239`; crypto_major avg `-0.0342` n `8`; equity avg `-0.0679` n `163`; fx avg `0.0325` n `6`; index avg `-0.0043` n `27`; metal avg `0.0583` n `20`; unknown avg `4.4042` n `1262`
- 4h: commodity avg `-0.0464` n `13`; crypto_alt avg `0.1351` n `239`; crypto_major avg `-0.0119` n `8`; equity avg `0.5106` n `163`; fx avg `-0.0708` n `6`; index avg `0.0721` n `27`; metal avg `-0.2604` n `20`; unknown avg `92.2119` n `1182`
- 24h: commodity avg `-0.1984` n `13`; crypto_alt avg `1.0615` n `239`; crypto_major avg `1.3481` n `8`; equity avg `1.8308` n `163`; fx avg `-0.0843` n `6`; index avg `0.1641` n `27`; metal avg `-0.9374` n `20`; unknown avg `5.6869` n `1097`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
