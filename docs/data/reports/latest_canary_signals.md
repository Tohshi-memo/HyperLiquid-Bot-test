# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T02:52:28.141393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.0455` n `230`; crypto_major avg `-0.0879` n `8`; equity avg `0.0135` n `112`; fx avg `0.0011` n `6`; index avg `0.0004` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0695` n `784`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.0655` n `230`; crypto_major avg `-0.1388` n `8`; equity avg `0.0204` n `112`; fx avg `-0.0041` n `6`; index avg `0.0025` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.0439` n `784`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `0.0167` n `230`; crypto_major avg `-0.2617` n `8`; equity avg `-0.0309` n `112`; fx avg `0.004` n `6`; index avg `-0.001` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.1557` n `784`
- 24h: commodity avg `0.2084` n `12`; crypto_alt avg `1.6063` n `230`; crypto_major avg `0.7702` n `8`; equity avg `0.5587` n `112`; fx avg `0.0003` n `6`; index avg `0.0278` n `25`; metal avg `0.0263` n `20`; unknown avg `0.0198` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
