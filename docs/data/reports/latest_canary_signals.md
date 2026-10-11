# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T23:22:29.022922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1466` n `13`; crypto_alt avg `-0.0169` n `235`; crypto_major avg `-0.0284` n `8`; equity avg `0.017` n `150`; fx avg `0.0007` n `6`; index avg `0.0216` n `26`; metal avg `0.0668` n `20`; unknown avg `0.0497` n `1134`
- 1h: commodity avg `-0.1449` n `13`; crypto_alt avg `0.2945` n `235`; crypto_major avg `0.1031` n `8`; equity avg `0.1092` n `150`; fx avg `0.0069` n `6`; index avg `0.0232` n `26`; metal avg `0.0623` n `20`; unknown avg `0.8346` n `1124`
- 4h: commodity avg `-0.054` n `13`; crypto_alt avg `0.1245` n `235`; crypto_major avg `-0.0954` n `8`; equity avg `0.1067` n `150`; fx avg `-0.0172` n `6`; index avg `0.0263` n `26`; metal avg `0.0079` n `20`; unknown avg `-0.2559` n `1090`
- 24h: commodity avg `0.0691` n `13`; crypto_alt avg `2.1012` n `235`; crypto_major avg `0.7523` n `8`; equity avg `0.3501` n `150`; fx avg `0.0072` n `6`; index avg `0.0581` n `26`; metal avg `0.0717` n `20`; unknown avg `0.6328` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
