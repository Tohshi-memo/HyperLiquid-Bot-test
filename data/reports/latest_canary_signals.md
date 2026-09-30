# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T21:22:38.330426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.0421` n `234`; crypto_major avg `0.0667` n `8`; equity avg `-0.0226` n `142`; fx avg `0.0129` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0` n `20`; unknown avg `3.8883` n `975`
- 1h: commodity avg `-0.0641` n `12`; crypto_alt avg `-0.4267` n `234`; crypto_major avg `0.0712` n `8`; equity avg `-0.2003` n `142`; fx avg `0.0158` n `6`; index avg `-0.0315` n `26`; metal avg `0.0395` n `20`; unknown avg `4.3931` n `931`
- 4h: commodity avg `-0.0998` n `12`; crypto_alt avg `-1.1605` n `234`; crypto_major avg `-0.3732` n `8`; equity avg `-0.1586` n `142`; fx avg `0.036` n `6`; index avg `-0.0793` n `26`; metal avg `0.095` n `20`; unknown avg `3.0273` n `887`
- 24h: commodity avg `0.2688` n `12`; crypto_alt avg `-0.065` n `234`; crypto_major avg `0.8835` n `8`; equity avg `-0.4952` n `142`; fx avg `0.1075` n `6`; index avg `-0.0641` n `26`; metal avg `-0.209` n `20`; unknown avg `788.4044` n `788`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
