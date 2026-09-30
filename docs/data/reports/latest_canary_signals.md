# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T16:22:36.074547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.0082` n `234`; crypto_major avg `0.0815` n `8`; equity avg `0.0059` n `142`; fx avg `-0.0008` n `6`; index avg `-0.0102` n `26`; metal avg `0.0274` n `20`; unknown avg `-0.2176` n `969`
- 1h: commodity avg `-0.0829` n `12`; crypto_alt avg `0.9632` n `234`; crypto_major avg `0.8631` n `8`; equity avg `0.1395` n `142`; fx avg `-0.034` n `6`; index avg `0.0215` n `26`; metal avg `0.0271` n `20`; unknown avg `-0.1834` n `961`
- 4h: commodity avg `0.2002` n `12`; crypto_alt avg `0.6464` n `234`; crypto_major avg `0.3676` n `8`; equity avg `0.2484` n `142`; fx avg `-0.0157` n `6`; index avg `0.1422` n `26`; metal avg `-0.1061` n `20`; unknown avg `4.86` n `875`
- 24h: commodity avg `0.1799` n `12`; crypto_alt avg `1.1207` n `234`; crypto_major avg `0.9209` n `8`; equity avg `-0.0629` n `142`; fx avg `0.069` n `6`; index avg `0.1705` n `26`; metal avg `0.0352` n `20`; unknown avg `14.7303` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
