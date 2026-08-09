# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T02:24:34.675214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.096` n `230`; crypto_major avg `0.0498` n `8`; equity avg `0.014` n `112`; fx avg `-0.0019` n `6`; index avg `0.0031` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0385` n `784`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `-0.0027` n `230`; crypto_major avg `-0.1177` n `8`; equity avg `-0.0423` n `112`; fx avg `0.0008` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0176` n `20`; unknown avg `-0.1284` n `784`
- 4h: commodity avg `0.0376` n `12`; crypto_alt avg `0.0324` n `230`; crypto_major avg `-0.2062` n `8`; equity avg `-0.0151` n `112`; fx avg `0.006` n `6`; index avg `0.0007` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.1754` n `784`
- 24h: commodity avg `0.231` n `12`; crypto_alt avg `1.7013` n `230`; crypto_major avg `0.9313` n `8`; equity avg `0.4475` n `112`; fx avg `-0.007` n `6`; index avg `0.03` n `25`; metal avg `0.026` n `20`; unknown avg `0.1575` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
