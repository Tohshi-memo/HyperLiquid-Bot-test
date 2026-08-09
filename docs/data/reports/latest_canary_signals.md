# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T23:07:25.682708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.0993` n `230`; crypto_major avg `-0.0169` n `8`; equity avg `0.0772` n `112`; fx avg `0.0089` n `6`; index avg `0.0264` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0263` n `785`
- 1h: commodity avg `-0.0782` n `12`; crypto_alt avg `-0.8303` n `230`; crypto_major avg `-0.7775` n `8`; equity avg `-0.0355` n `112`; fx avg `0.01` n `6`; index avg `0.0232` n `25`; metal avg `0.007` n `20`; unknown avg `0.8817` n `785`
- 4h: commodity avg `0.2708` n `12`; crypto_alt avg `-0.3863` n `230`; crypto_major avg `-0.4535` n `8`; equity avg `-0.0995` n `112`; fx avg `0.0063` n `6`; index avg `-0.033` n `25`; metal avg `-0.1182` n `20`; unknown avg `-0.0805` n `785`
- 24h: commodity avg `0.378` n `12`; crypto_alt avg `1.0022` n `230`; crypto_major avg `0.0046` n `8`; equity avg `0.057` n `112`; fx avg `0.0099` n `6`; index avg `0.0066` n `25`; metal avg `-0.0424` n `20`; unknown avg `-0.3376` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
