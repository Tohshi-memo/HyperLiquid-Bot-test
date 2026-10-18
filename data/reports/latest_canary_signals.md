# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T05:37:40.291919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `-0.4525` n `237`; crypto_major avg `-0.2667` n `8`; equity avg `-0.088` n `151`; fx avg `0.0089` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.2424` n `1193`
- 1h: commodity avg `-0.0284` n `13`; crypto_alt avg `-0.7129` n `237`; crypto_major avg `-0.3602` n `8`; equity avg `-0.0513` n `151`; fx avg `0.0142` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0097` n `20`; unknown avg `-0.0613` n `1191`
- 4h: commodity avg `0.0473` n `13`; crypto_alt avg `-0.9914` n `237`; crypto_major avg `-0.2268` n `8`; equity avg `-0.0898` n `151`; fx avg `-0.0041` n `6`; index avg `-0.0014` n `26`; metal avg `0.0107` n `20`; unknown avg `-0.1724` n `1185`
- 24h: commodity avg `-0.1426` n `13`; crypto_alt avg `-3.132` n `236`; crypto_major avg `-0.9154` n `8`; equity avg `-0.9822` n `151`; fx avg `-0.0319` n `6`; index avg `-0.1245` n `26`; metal avg `-0.0543` n `20`; unknown avg `3.6619` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.169`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
