# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T23:37:25.305852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.2152` n `239`; crypto_major avg `0.3447` n `8`; equity avg `0.3062` n `162`; fx avg `-0.001` n `6`; index avg `0.0445` n `27`; metal avg `0.043` n `20`; unknown avg `-0.0489` n `1265`
- 1h: commodity avg `-0.2105` n `13`; crypto_alt avg `0.2294` n `239`; crypto_major avg `0.3647` n `8`; equity avg `0.91` n `162`; fx avg `-0.0029` n `6`; index avg `0.1835` n `27`; metal avg `0.3096` n `20`; unknown avg `0.0379` n `1231`
- 4h: commodity avg `-0.3` n `13`; crypto_alt avg `0.8636` n `239`; crypto_major avg `0.9435` n `8`; equity avg `1.1595` n `162`; fx avg `0.0176` n `6`; index avg `0.1878` n `27`; metal avg `0.3552` n `20`; unknown avg `0.6704` n `1185`
- 24h: commodity avg `-0.291` n `13`; crypto_alt avg `3.6546` n `239`; crypto_major avg `4.963` n `8`; equity avg `2.3839` n `162`; fx avg `0.0155` n `6`; index avg `0.2952` n `27`; metal avg `0.5594` n `20`; unknown avg `3.4899` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
