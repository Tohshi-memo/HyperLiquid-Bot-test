# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T20:07:34.051219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.157` n `234`; crypto_major avg `0.1332` n `8`; equity avg `-0.1858` n `142`; fx avg `0.0069` n `6`; index avg `-0.0448` n `26`; metal avg `-0.0217` n `20`; unknown avg `2.9919` n `929`
- 1h: commodity avg `0.0072` n `12`; crypto_alt avg `-0.3323` n `234`; crypto_major avg `-0.4045` n `8`; equity avg `-0.332` n `142`; fx avg `0.0119` n `6`; index avg `-0.0824` n `26`; metal avg `-0.006` n `20`; unknown avg `15.3651` n `929`
- 4h: commodity avg `-0.1317` n `12`; crypto_alt avg `-1.5548` n `234`; crypto_major avg `-0.7212` n `8`; equity avg `-0.3722` n `142`; fx avg `0.0036` n `6`; index avg `-0.1682` n `26`; metal avg `0.0197` n `20`; unknown avg `5.4678` n `929`
- 24h: commodity avg `0.3764` n `12`; crypto_alt avg `-0.0583` n `234`; crypto_major avg `0.4541` n `8`; equity avg `-0.4032` n `142`; fx avg `0.0668` n `6`; index avg `-0.0585` n `26`; metal avg `-0.2299` n `20`; unknown avg `8.8945` n `790`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
