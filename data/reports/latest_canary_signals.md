# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T08:05:17.827452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.2193` n `230`; crypto_major avg `0.1719` n `8`; equity avg `0.0178` n `112`; fx avg `0.0016` n `6`; index avg `0.0043` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.005` n `785`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `0.0956` n `230`; crypto_major avg `0.0938` n `8`; equity avg `-0.0378` n `112`; fx avg `-0.0012` n `6`; index avg `0.0144` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.0384` n `785`
- 4h: commodity avg `0.0398` n `12`; crypto_alt avg `0.1288` n `230`; crypto_major avg `0.3198` n `8`; equity avg `0.0666` n `112`; fx avg `-0.0214` n `6`; index avg `0.0066` n `25`; metal avg `0.0119` n `20`; unknown avg `0.0083` n `752`
- 24h: commodity avg `0.2439` n `12`; crypto_alt avg `1.4961` n `230`; crypto_major avg `0.6962` n `8`; equity avg `0.6509` n `112`; fx avg `-0.0181` n `6`; index avg `0.0662` n `25`; metal avg `0.037` n `20`; unknown avg `0.5149` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
