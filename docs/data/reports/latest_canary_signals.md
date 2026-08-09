# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T00:22:23.178456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0136` n `230`; crypto_major avg `0.0153` n `8`; equity avg `0.0166` n `112`; fx avg `0.011` n `6`; index avg `-0.0008` n `25`; metal avg `0.0163` n `20`; unknown avg `0.0105` n `784`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `0.0606` n `230`; crypto_major avg `0.0624` n `8`; equity avg `-0.0087` n `112`; fx avg `0.0096` n `6`; index avg `-0.0008` n `25`; metal avg `0.0192` n `20`; unknown avg `-0.0035` n `784`
- 4h: commodity avg `-0.01` n `12`; crypto_alt avg `0.001` n `230`; crypto_major avg `-0.2309` n `8`; equity avg `0.046` n `112`; fx avg `0.0164` n `6`; index avg `0.0072` n `25`; metal avg `0.0365` n `20`; unknown avg `-0.117` n `784`
- 24h: commodity avg `0.2176` n `12`; crypto_alt avg `1.8592` n `230`; crypto_major avg `1.2406` n `8`; equity avg `0.5288` n `112`; fx avg `0.0025` n `6`; index avg `0.0602` n `25`; metal avg `0.0112` n `20`; unknown avg `0.2187` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
