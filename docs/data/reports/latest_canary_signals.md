# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T19:52:28.866566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `13`; crypto_alt avg `0.2026` n `237`; crypto_major avg `0.2284` n `8`; equity avg `0.0567` n `151`; fx avg `-0.0002` n `6`; index avg `0.0224` n `26`; metal avg `0.022` n `20`; unknown avg `41.9731` n `1197`
- 1h: commodity avg `0.0971` n `13`; crypto_alt avg `0.179` n `237`; crypto_major avg `0.3035` n `8`; equity avg `0.0119` n `151`; fx avg `-0.0072` n `6`; index avg `0.0004` n `26`; metal avg `-0.0089` n `20`; unknown avg `52.2793` n `1193`
- 4h: commodity avg `0.303` n `13`; crypto_alt avg `0.6346` n `237`; crypto_major avg `0.6365` n `8`; equity avg `-0.0071` n `151`; fx avg `0.0097` n `6`; index avg `-0.0254` n `26`; metal avg `-0.0872` n `20`; unknown avg `12.9162` n `1173`
- 24h: commodity avg `-0.0554` n `13`; crypto_alt avg `2.7709` n `237`; crypto_major avg `1.9283` n `8`; equity avg `0.1426` n `151`; fx avg `0.0286` n `6`; index avg `0.0164` n `26`; metal avg `-0.0015` n `20`; unknown avg `5.9688` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
