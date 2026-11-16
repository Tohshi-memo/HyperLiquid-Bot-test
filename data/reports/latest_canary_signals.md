# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T08:37:41.274523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0733` n `13`; crypto_alt avg `0.0886` n `239`; crypto_major avg `0.0519` n `8`; equity avg `-0.0578` n `162`; fx avg `-0.027` n `6`; index avg `-0.0062` n `27`; metal avg `-0.048` n `20`; unknown avg `0.142` n `1263`
- 1h: commodity avg `-0.0266` n `13`; crypto_alt avg `-0.4563` n `239`; crypto_major avg `-0.5712` n `8`; equity avg `0.0337` n `162`; fx avg `-0.0191` n `6`; index avg `0.0301` n `27`; metal avg `-0.0861` n `20`; unknown avg `3.3445` n `1219`
- 4h: commodity avg `0.0274` n `13`; crypto_alt avg `-0.8054` n `239`; crypto_major avg `-0.563` n `8`; equity avg `-0.5489` n `162`; fx avg `-0.0567` n `6`; index avg `-0.0212` n `27`; metal avg `-0.1018` n `20`; unknown avg `2.8614` n `1077`
- 24h: commodity avg `-0.3174` n `13`; crypto_alt avg `0.3486` n `239`; crypto_major avg `0.6236` n `8`; equity avg `-0.1895` n `162`; fx avg `-0.0741` n `6`; index avg `0.0238` n `27`; metal avg `0.0308` n `20`; unknown avg `3.5476` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
