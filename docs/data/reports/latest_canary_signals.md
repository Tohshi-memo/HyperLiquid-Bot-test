# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T02:37:29.261289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0409` n `13`; crypto_alt avg `0.3901` n `234`; crypto_major avg `0.0889` n `8`; equity avg `0.1034` n `142`; fx avg `0.0081` n `6`; index avg `0.0283` n `26`; metal avg `0.0051` n `20`; unknown avg `0.2242` n `974`
- 1h: commodity avg `0.3394` n `13`; crypto_alt avg `0.0216` n `234`; crypto_major avg `-0.1198` n `8`; equity avg `0.1934` n `142`; fx avg `-0.0303` n `6`; index avg `0.0553` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.2784` n `972`
- 4h: commodity avg `-0.038` n `13`; crypto_alt avg `-0.0326` n `234`; crypto_major avg `-0.4274` n `8`; equity avg `0.3363` n `142`; fx avg `0.0962` n `6`; index avg `0.1263` n `26`; metal avg `-0.0056` n `20`; unknown avg `1.2899` n `942`
- 24h: commodity avg `0.098` n `13`; crypto_alt avg `0.6817` n `234`; crypto_major avg `0.6204` n `8`; equity avg `0.3734` n `142`; fx avg `0.2494` n `6`; index avg `0.1726` n `26`; metal avg `-0.1399` n `20`; unknown avg `780.1946` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
