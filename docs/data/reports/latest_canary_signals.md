# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T18:52:28.660646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.0245` n `230`; crypto_major avg `-0.0195` n `8`; equity avg `-0.0125` n `112`; fx avg `0.0005` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0056` n `20`; unknown avg `-0.1073` n `784`
- 1h: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0931` n `230`; crypto_major avg `-0.2713` n `8`; equity avg `-0.0408` n `112`; fx avg `0.006` n `6`; index avg `-0.0012` n `25`; metal avg `0.0001` n `20`; unknown avg `0.041` n `784`
- 4h: commodity avg `0.1203` n `12`; crypto_alt avg `0.4778` n `230`; crypto_major avg `-0.283` n `8`; equity avg `0.1777` n `112`; fx avg `0.0003` n `6`; index avg `0.0094` n `25`; metal avg `0.0099` n `20`; unknown avg `0.1577` n `784`
- 24h: commodity avg `-0.1451` n `12`; crypto_alt avg `1.7487` n `230`; crypto_major avg `1.7145` n `8`; equity avg `1.0569` n `112`; fx avg `0.0085` n `6`; index avg `0.1003` n `25`; metal avg `0.1058` n `20`; unknown avg `0.1435` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
