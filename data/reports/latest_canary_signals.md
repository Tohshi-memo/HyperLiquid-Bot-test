# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T02:07:24.324812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0656` n `230`; crypto_major avg `-0.0528` n `8`; equity avg `-0.0006` n `112`; fx avg `-0.0033` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0108` n `784`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `-0.1101` n `230`; crypto_major avg `-0.2503` n `8`; equity avg `-0.0902` n `112`; fx avg `0.0018` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0268` n `20`; unknown avg `0.0463` n `784`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.2885` n `8`; equity avg `-0.0271` n `112`; fx avg `0.0063` n `6`; index avg `0.0007` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.1543` n `784`
- 24h: commodity avg `0.2191` n `12`; crypto_alt avg `1.6325` n `230`; crypto_major avg `0.8156` n `8`; equity avg `0.3879` n `112`; fx avg `-0.0045` n `6`; index avg `0.0236` n `25`; metal avg `0.0068` n `20`; unknown avg `0.1453` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
