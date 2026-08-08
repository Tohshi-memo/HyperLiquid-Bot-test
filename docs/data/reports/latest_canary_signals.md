# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T22:37:29.641921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.0414` n `230`; crypto_major avg `0.0027` n `8`; equity avg `0.023` n `112`; fx avg `0.0021` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.5165` n `784`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `-0.0467` n `230`; crypto_major avg `-0.1987` n `8`; equity avg `0.0045` n `112`; fx avg `0.0035` n `6`; index avg `0.0019` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.3738` n `784`
- 4h: commodity avg `0.0646` n `12`; crypto_alt avg `-0.0163` n `230`; crypto_major avg `-0.1121` n `8`; equity avg `0.1444` n `112`; fx avg `0.0009` n `6`; index avg `0.0097` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.2808` n `784`
- 24h: commodity avg `0.2341` n `12`; crypto_alt avg `1.9468` n `230`; crypto_major avg `1.3487` n `8`; equity avg `0.6632` n `112`; fx avg `-0.009` n `6`; index avg `0.0242` n `25`; metal avg `0.0082` n `20`; unknown avg `0.1903` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
