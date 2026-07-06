# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T23:22:31.868221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0349` n `12`; crypto_alt avg `-0.1854` n `229`; crypto_major avg `-0.2704` n `8`; equity avg `-0.2259` n `91`; fx avg `-0.0116` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.1561` n `763`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.3182` n `229`; crypto_major avg `-0.4528` n `8`; equity avg `-0.4622` n `91`; fx avg `-0.0009` n `6`; index avg `-0.1003` n `25`; metal avg `-0.0272` n `20`; unknown avg `0.0893` n `763`
- 4h: commodity avg `0.0296` n `12`; crypto_alt avg `0.1455` n `229`; crypto_major avg `0.0594` n `8`; equity avg `-0.4631` n `91`; fx avg `0.0158` n `6`; index avg `-0.0881` n `25`; metal avg `-0.0255` n `20`; unknown avg `-0.3801` n `763`
- 24h: commodity avg `0.2519` n `12`; crypto_alt avg `0.1827` n `229`; crypto_major avg `-0.5283` n `8`; equity avg `-1.2435` n `90`; fx avg `0.1245` n `6`; index avg `-0.0611` n `25`; metal avg `-0.3772` n `20`; unknown avg `-0.5029` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
