# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T05:07:27.270759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.1214` n `234`; crypto_major avg `-0.1657` n `8`; equity avg `0.1528` n `142`; fx avg `-0.0082` n `6`; index avg `0.0549` n `26`; metal avg `0.0416` n `20`; unknown avg `0.2873` n `972`
- 1h: commodity avg `-0.104` n `13`; crypto_alt avg `0.0226` n `234`; crypto_major avg `0.3176` n `8`; equity avg `0.2617` n `142`; fx avg `-0.0341` n `6`; index avg `0.0606` n `26`; metal avg `0.0872` n `20`; unknown avg `0.1881` n `972`
- 4h: commodity avg `-0.7246` n `13`; crypto_alt avg `0.6548` n `234`; crypto_major avg `0.4354` n `8`; equity avg `0.8971` n `142`; fx avg `-0.0394` n `6`; index avg `0.2078` n `26`; metal avg `0.2238` n `20`; unknown avg `0.4243` n `966`
- 24h: commodity avg `-0.6525` n `13`; crypto_alt avg `1.3417` n `234`; crypto_major avg `1.3019` n `8`; equity avg `0.8881` n `142`; fx avg `0.1451` n `6`; index avg `0.2681` n `26`; metal avg `0.0675` n `20`; unknown avg `776.9942` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
