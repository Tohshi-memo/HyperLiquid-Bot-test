# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T13:07:26.765646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.1983` n `231`; crypto_major avg `0.1533` n `8`; equity avg `-0.0111` n `128`; fx avg `-0.0007` n `6`; index avg `-0.006` n `26`; metal avg `0.009` n `20`; unknown avg `0.0087` n `793`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.2493` n `231`; crypto_major avg `0.2464` n `8`; equity avg `-0.033` n `128`; fx avg `-0.0017` n `6`; index avg `0.0158` n `26`; metal avg `0.0216` n `20`; unknown avg `0.1419` n `793`
- 4h: commodity avg `0.0141` n `12`; crypto_alt avg `1.1285` n `231`; crypto_major avg `0.5761` n `8`; equity avg `-0.0035` n `128`; fx avg `-0.0025` n `6`; index avg `0.0274` n `26`; metal avg `0.0033` n `20`; unknown avg `0.5043` n `789`
- 24h: commodity avg `-0.0198` n `12`; crypto_alt avg `2.0888` n `231`; crypto_major avg `1.4316` n `8`; equity avg `0.3291` n `128`; fx avg `0.0137` n `6`; index avg `0.0845` n `26`; metal avg `0.0906` n `20`; unknown avg `0.0934` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
