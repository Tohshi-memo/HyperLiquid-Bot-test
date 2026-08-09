# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T12:22:26.303284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0533` n `12`; crypto_alt avg `0.0735` n `230`; crypto_major avg `0.06` n `8`; equity avg `0.0378` n `112`; fx avg `-0.0041` n `6`; index avg `0.002` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0224` n `785`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.0122` n `230`; crypto_major avg `-0.1059` n `8`; equity avg `0.0143` n `112`; fx avg `-0.0017` n `6`; index avg `-0.002` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0005` n `785`
- 4h: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0274` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `-0.0385` n `112`; fx avg `0.0005` n `6`; index avg `-0.0163` n `25`; metal avg `-0.0114` n `20`; unknown avg `0.0088` n `785`
- 24h: commodity avg `0.1827` n `12`; crypto_alt avg `1.0574` n `230`; crypto_major avg `0.197` n `8`; equity avg `0.403` n `112`; fx avg `-0.0081` n `6`; index avg `0.0344` n `25`; metal avg `0.0229` n `20`; unknown avg `0.2531` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
