# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T09:57:07.069055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0611` n `13`; crypto_alt avg `-0.1009` n `236`; crypto_major avg `-0.0646` n `8`; equity avg `-0.156` n `151`; fx avg `-0.0075` n `6`; index avg `-0.0504` n `26`; metal avg `-0.026` n `20`; unknown avg `1.4589` n `1136`
- 1h: commodity avg `0.0566` n `13`; crypto_alt avg `-0.1445` n `236`; crypto_major avg `-0.2257` n `8`; equity avg `-0.1413` n `151`; fx avg `-0.0023` n `6`; index avg `-0.038` n `26`; metal avg `-0.0561` n `20`; unknown avg `-0.1754` n `1134`
- 4h: commodity avg `0.0071` n `13`; crypto_alt avg `0.122` n `236`; crypto_major avg `0.0848` n `8`; equity avg `-0.4479` n `151`; fx avg `0.0039` n `6`; index avg `-0.0978` n `26`; metal avg `-0.0231` n `20`; unknown avg `-0.0399` n `1048`
- 24h: commodity avg `0.0215` n `13`; crypto_alt avg `3.8735` n `236`; crypto_major avg `1.7693` n `8`; equity avg `2.4794` n `151`; fx avg `0.0037` n `6`; index avg `0.3085` n `26`; metal avg `0.2119` n `20`; unknown avg `27.0426` n `872`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0969`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0862`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
