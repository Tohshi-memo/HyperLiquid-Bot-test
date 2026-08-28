# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T09:52:26.054316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0726` n `12`; crypto_alt avg `-0.0234` n `231`; crypto_major avg `-0.0859` n `8`; equity avg `0.0034` n `127`; fx avg `-0.007` n `6`; index avg `0.0105` n `26`; metal avg `0.0719` n `20`; unknown avg `-0.0116` n `792`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `-0.0036` n `231`; crypto_major avg `-0.4012` n `8`; equity avg `-0.0781` n `127`; fx avg `0.0057` n `6`; index avg `0.0042` n `26`; metal avg `0.1633` n `20`; unknown avg `-0.0516` n `792`
- 4h: commodity avg `-0.1131` n `12`; crypto_alt avg `-0.356` n `231`; crypto_major avg `-0.7138` n `8`; equity avg `-0.1256` n `127`; fx avg `-0.038` n `6`; index avg `0.022` n `26`; metal avg `0.5537` n `20`; unknown avg `-0.0663` n `760`
- 24h: commodity avg `0.1575` n `12`; crypto_alt avg `-1.3313` n `231`; crypto_major avg `-0.9482` n `8`; equity avg `-1.24` n `127`; fx avg `-0.096` n `6`; index avg `-0.033` n `26`; metal avg `0.7538` n `20`; unknown avg `0.2229` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
