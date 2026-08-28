# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T13:52:29.314474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `12`; crypto_alt avg `0.0309` n `231`; crypto_major avg `0.086` n `8`; equity avg `0.0018` n `127`; fx avg `-0.0138` n `6`; index avg `0.006` n `26`; metal avg `0.0906` n `20`; unknown avg `0.025` n `793`
- 1h: commodity avg `0.106` n `12`; crypto_alt avg `-0.1604` n `231`; crypto_major avg `0.202` n `8`; equity avg `-0.2363` n `127`; fx avg `-0.0032` n `6`; index avg `-0.0076` n `26`; metal avg `0.1767` n `20`; unknown avg `-0.128` n `792`
- 4h: commodity avg `-0.1251` n `12`; crypto_alt avg `-0.0007` n `231`; crypto_major avg `0.2029` n `8`; equity avg `-0.154` n `127`; fx avg `0.0172` n `6`; index avg `0.0116` n `26`; metal avg `0.1929` n `20`; unknown avg `-0.0288` n `792`
- 24h: commodity avg `-0.2319` n `12`; crypto_alt avg `-0.8608` n `231`; crypto_major avg `-0.0571` n `8`; equity avg `-0.8094` n `127`; fx avg `-0.1169` n `6`; index avg `0.0517` n `26`; metal avg `1.0207` n `20`; unknown avg `0.4448` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
