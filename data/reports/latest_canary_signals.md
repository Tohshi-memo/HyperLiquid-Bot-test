# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:22:28.717315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1622` n `230`; crypto_major avg `0.1471` n `8`; equity avg `-0.0094` n `112`; fx avg `-0.0014` n `6`; index avg `0.0101` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0186` n `784`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `0.2103` n `230`; crypto_major avg `0.2639` n `8`; equity avg `-0.0154` n `112`; fx avg `0.0005` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0096` n `20`; unknown avg `-0.1132` n `784`
- 4h: commodity avg `0.0741` n `12`; crypto_alt avg `0.3865` n `230`; crypto_major avg `0.3766` n `8`; equity avg `0.2219` n `112`; fx avg `-0.0118` n `6`; index avg `0.0414` n `25`; metal avg `-0.0444` n `20`; unknown avg `-0.2762` n `784`
- 24h: commodity avg `-0.0614` n `12`; crypto_alt avg `0.6226` n `230`; crypto_major avg `0.4819` n `8`; equity avg `1.2345` n `112`; fx avg `-0.0158` n `6`; index avg `0.1036` n `25`; metal avg `0.0462` n `20`; unknown avg `-0.1065` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
