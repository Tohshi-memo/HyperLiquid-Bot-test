# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T12:07:31.675336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `12`; crypto_alt avg `-0.054` n `231`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0053` n `127`; fx avg `-0.0112` n `6`; index avg `0.0074` n `26`; metal avg `0.0252` n `20`; unknown avg `-0.0355` n `792`
- 1h: commodity avg `-0.1746` n `12`; crypto_alt avg `-0.2473` n `231`; crypto_major avg `-0.3021` n `8`; equity avg `-0.1467` n `127`; fx avg `-0.0168` n `6`; index avg `0.0032` n `26`; metal avg `0.0562` n `20`; unknown avg `0.1116` n `792`
- 4h: commodity avg `-0.1605` n `12`; crypto_alt avg `0.0823` n `231`; crypto_major avg `-0.4561` n `8`; equity avg `-0.0625` n `127`; fx avg `0.0365` n `6`; index avg `0.0053` n `26`; metal avg `0.1232` n `20`; unknown avg `0.1026` n `792`
- 24h: commodity avg `-0.097` n `12`; crypto_alt avg `-0.21` n `231`; crypto_major avg `0.1109` n `8`; equity avg `-0.9195` n `127`; fx avg `-0.0348` n `6`; index avg `-0.0231` n `26`; metal avg `0.7221` n `20`; unknown avg `0.5281` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
