# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T10:07:27.013334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.1302` n `239`; crypto_major avg `0.2654` n `8`; equity avg `0.2518` n `165`; fx avg `-0.0209` n `6`; index avg `0.0258` n `27`; metal avg `0.0588` n `20`; unknown avg `-0.0096` n `1252`
- 1h: commodity avg `-0.1105` n `13`; crypto_alt avg `0.0554` n `239`; crypto_major avg `0.2319` n `8`; equity avg `-0.4012` n `165`; fx avg `0.0208` n `6`; index avg `-0.0583` n `27`; metal avg `0.0199` n `20`; unknown avg `1.7405` n `1254`
- 4h: commodity avg `-0.4477` n `13`; crypto_alt avg `-0.0611` n `239`; crypto_major avg `-0.1744` n `8`; equity avg `-0.6933` n `165`; fx avg `-0.0415` n `6`; index avg `-0.0245` n `27`; metal avg `0.1305` n `20`; unknown avg `9.367` n `1192`
- 24h: commodity avg `-0.7289` n `13`; crypto_alt avg `-3.3858` n `239`; crypto_major avg `-2.9648` n `8`; equity avg `-7.7998` n `165`; fx avg `-0.0953` n `6`; index avg `-0.7981` n `27`; metal avg `-1.4426` n `20`; unknown avg `22.952` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
