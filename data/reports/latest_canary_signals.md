# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T18:07:27.890670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.0793` n `230`; crypto_major avg `-0.1098` n `8`; equity avg `-0.0268` n `112`; fx avg `-0.0002` n `6`; index avg `0.0013` n `25`; metal avg `0.004` n `20`; unknown avg `0.0381` n `784`
- 1h: commodity avg `-0.0502` n `12`; crypto_alt avg `-0.0483` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `0.0633` n `112`; fx avg `-0.001` n `6`; index avg `0.0056` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0819` n `784`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.8264` n `230`; crypto_major avg `0.5111` n `8`; equity avg `0.1582` n `112`; fx avg `-0.0065` n `6`; index avg `0.0224` n `25`; metal avg `0.0172` n `20`; unknown avg `0.0306` n `784`
- 24h: commodity avg `-0.2141` n `12`; crypto_alt avg `1.5419` n `230`; crypto_major avg `1.6016` n `8`; equity avg `0.9268` n `112`; fx avg `0.0098` n `6`; index avg `0.0732` n `25`; metal avg `0.1018` n `20`; unknown avg `0.15` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
