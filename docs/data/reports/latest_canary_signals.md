# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T12:22:37.912016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.0363` n `239`; crypto_major avg `-0.0649` n `8`; equity avg `-0.2118` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0194` n `27`; metal avg `0.0116` n `20`; unknown avg `-0.1882` n `1260`
- 1h: commodity avg `0.0859` n `13`; crypto_alt avg `0.2654` n `239`; crypto_major avg `0.1319` n `8`; equity avg `-0.0156` n `162`; fx avg `0.0125` n `6`; index avg `-0.0024` n `27`; metal avg `0.0916` n `20`; unknown avg `90.0247` n `1254`
- 4h: commodity avg `0.1097` n `13`; crypto_alt avg `0.8628` n `239`; crypto_major avg `1.4589` n `8`; equity avg `0.7527` n `162`; fx avg `-0.0186` n `6`; index avg `0.0706` n `27`; metal avg `0.1406` n `20`; unknown avg `43.4629` n `1200`
- 24h: commodity avg `0.8667` n `13`; crypto_alt avg `0.268` n `239`; crypto_major avg `-1.4192` n `8`; equity avg `-0.3061` n `162`; fx avg `-0.0147` n `6`; index avg `0.0661` n `27`; metal avg `-0.3054` n `20`; unknown avg `1.9777` n `1075`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
