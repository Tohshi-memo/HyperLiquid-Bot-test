# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T06:22:26.469432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.0676` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `0.0926` n `112`; fx avg `0.0128` n `6`; index avg `0.0175` n `25`; metal avg `-0.0176` n `20`; unknown avg `54.7136` n `785`
- 1h: commodity avg `-0.0595` n `12`; crypto_alt avg `0.2589` n `230`; crypto_major avg `0.2388` n `8`; equity avg `0.1221` n `112`; fx avg `0.0324` n `6`; index avg `0.0058` n `25`; metal avg `0.0906` n `20`; unknown avg `57.2181` n `753`
- 4h: commodity avg `-0.1041` n `12`; crypto_alt avg `0.36` n `230`; crypto_major avg `0.3337` n `8`; equity avg `0.184` n `112`; fx avg `0.052` n `6`; index avg `0.0318` n `25`; metal avg `0.1283` n `20`; unknown avg `57.2002` n `753`
- 24h: commodity avg `0.2393` n `12`; crypto_alt avg `0.8326` n `230`; crypto_major avg `0.1166` n `8`; equity avg `-0.1865` n `112`; fx avg `0.1835` n `6`; index avg `0.0568` n `25`; metal avg `-0.0406` n `20`; unknown avg `56.8819` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
