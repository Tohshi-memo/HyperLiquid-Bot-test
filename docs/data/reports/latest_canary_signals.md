# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T02:07:26.364803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `13`; crypto_alt avg `0.1258` n `237`; crypto_major avg `0.0918` n `8`; equity avg `0.0985` n `151`; fx avg `0.0017` n `6`; index avg `0.0278` n `26`; metal avg `0.0415` n `20`; unknown avg `0.061` n `1192`
- 1h: commodity avg `-0.0451` n `13`; crypto_alt avg `0.4534` n `237`; crypto_major avg `0.2704` n `8`; equity avg `0.3172` n `151`; fx avg `-0.0256` n `6`; index avg `0.0883` n `26`; metal avg `0.1037` n `20`; unknown avg `0.0312` n `1192`
- 4h: commodity avg `-0.1783` n `13`; crypto_alt avg `2.0856` n `237`; crypto_major avg `1.3437` n `8`; equity avg `1.789` n `151`; fx avg `-0.0039` n `6`; index avg `0.2723` n `26`; metal avg `0.1718` n `20`; unknown avg `3.2688` n `1120`
- 24h: commodity avg `-0.415` n `13`; crypto_alt avg `0.1238` n `237`; crypto_major avg `0.9032` n `8`; equity avg `2.4077` n `151`; fx avg `-0.0208` n `6`; index avg `0.4678` n `26`; metal avg `0.3024` n `20`; unknown avg `2.7981` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2003`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0892`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0593`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
