# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T04:37:34.155148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.0073` n `234`; crypto_major avg `-0.0346` n `8`; equity avg `0.061` n `142`; fx avg `0.0022` n `6`; index avg `0.0255` n `26`; metal avg `0.0323` n `20`; unknown avg `0.0347` n `974`
- 1h: commodity avg `-0.2341` n `13`; crypto_alt avg `0.098` n `234`; crypto_major avg `0.1193` n `8`; equity avg `0.2611` n `142`; fx avg `-0.0129` n `6`; index avg `0.0786` n `26`; metal avg `0.0866` n `20`; unknown avg `-0.1017` n `966`
- 4h: commodity avg `-0.7561` n `13`; crypto_alt avg `0.807` n `234`; crypto_major avg `0.2056` n `8`; equity avg `0.9278` n `142`; fx avg `-0.023` n `6`; index avg `0.2427` n `26`; metal avg `0.2881` n `20`; unknown avg `0.3781` n `966`
- 24h: commodity avg `-0.5789` n `13`; crypto_alt avg `1.1934` n `234`; crypto_major avg `0.8523` n `8`; equity avg `0.4936` n `142`; fx avg `0.1733` n `6`; index avg `0.1794` n `26`; metal avg `-0.0332` n `20`; unknown avg `773.6562` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
