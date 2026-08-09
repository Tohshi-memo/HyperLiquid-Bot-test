# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T00:37:29.125884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.0576` n `230`; crypto_major avg `0.0088` n `8`; equity avg `0.0232` n `112`; fx avg `-0.0065` n `6`; index avg `0.0037` n `25`; metal avg `-0.0208` n `20`; unknown avg `1.0168` n `784`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0182` n `230`; crypto_major avg `0.0111` n `8`; equity avg `0.0222` n `112`; fx avg `0.0083` n `6`; index avg `0.0032` n `25`; metal avg `-0.0051` n `20`; unknown avg `1.0337` n `784`
- 4h: commodity avg `-0.0301` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `-0.2339` n `8`; equity avg `0.0266` n `112`; fx avg `0.0094` n `6`; index avg `0.0035` n `25`; metal avg `0.0102` n `20`; unknown avg `-0.0363` n `784`
- 24h: commodity avg `0.1918` n `12`; crypto_alt avg `1.8312` n `230`; crypto_major avg `1.2779` n `8`; equity avg `0.537` n `112`; fx avg `-0.0019` n `6`; index avg `0.0525` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.2374` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
