# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T21:07:32.024254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.034` n `230`; crypto_major avg `-0.0526` n `8`; equity avg `-0.0122` n `112`; fx avg `0.0061` n `6`; index avg `0.0004` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0221` n `785`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.053` n `230`; crypto_major avg `-0.0465` n `8`; equity avg `0.0127` n `112`; fx avg `0.0112` n `6`; index avg `-0.0013` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0896` n `785`
- 4h: commodity avg `0.1265` n `12`; crypto_alt avg `0.1674` n `230`; crypto_major avg `-0.2207` n `8`; equity avg `0.1087` n `112`; fx avg `0.0102` n `6`; index avg `0.0185` n `25`; metal avg `0.0258` n `20`; unknown avg `-0.3096` n `785`
- 24h: commodity avg `0.0983` n `12`; crypto_alt avg `1.3909` n `230`; crypto_major avg `0.0568` n `8`; equity avg `0.2163` n `112`; fx avg `0.0168` n `6`; index avg `0.0209` n `25`; metal avg `0.0975` n `20`; unknown avg `-0.2889` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
