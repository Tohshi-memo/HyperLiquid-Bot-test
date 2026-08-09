# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T01:37:27.239184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `12`; crypto_alt avg `-0.1922` n `230`; crypto_major avg `-0.1472` n `8`; equity avg `-0.0844` n `112`; fx avg `0.0` n `6`; index avg `-0.017` n `25`; metal avg `-0.0133` n `20`; unknown avg `0.0289` n `784`
- 1h: commodity avg `0.0526` n `12`; crypto_alt avg `-0.0964` n `230`; crypto_major avg `-0.1833` n `8`; equity avg `-0.0737` n `112`; fx avg `-0.0017` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.2291` n `784`
- 4h: commodity avg `0.0633` n `12`; crypto_alt avg `-0.1623` n `230`; crypto_major avg `-0.4364` n `8`; equity avg `-0.0754` n `112`; fx avg `0.0066` n `6`; index avg `-0.0032` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.1262` n `784`
- 24h: commodity avg `0.1845` n `12`; crypto_alt avg `1.5524` n `230`; crypto_major avg `0.868` n `8`; equity avg `0.4472` n `112`; fx avg `-0.0111` n `6`; index avg `0.0463` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.1888` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
