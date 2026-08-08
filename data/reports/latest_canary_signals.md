# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:16:05.365598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.0399` n `230`; crypto_major avg `0.0175` n `8`; equity avg `0.0291` n `112`; fx avg `-0.0017` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0018` n `784`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.3344` n `230`; crypto_major avg `0.1615` n `8`; equity avg `-0.0457` n `112`; fx avg `-0.0057` n `6`; index avg `-0.0037` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0076` n `784`
- 4h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.8241` n `230`; crypto_major avg `0.7774` n `8`; equity avg `0.1937` n `112`; fx avg `-0.0087` n `6`; index avg `0.0351` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.2358` n `784`
- 24h: commodity avg `-0.2947` n `12`; crypto_alt avg `1.2293` n `230`; crypto_major avg `1.0614` n `8`; equity avg `0.5259` n `112`; fx avg `0.0028` n `6`; index avg `0.0429` n `25`; metal avg `0.0881` n `20`; unknown avg `-0.1017` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
