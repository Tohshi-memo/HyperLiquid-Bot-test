# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T00:22:27.474247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `-0.2479` n `233`; crypto_major avg `-0.2079` n `8`; equity avg `-0.2483` n `136`; fx avg `-0.0168` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0373` n `20`; unknown avg `13.359` n `840`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `0.1192` n `233`; crypto_major avg `0.0489` n `8`; equity avg `-0.1552` n `136`; fx avg `0.0101` n `6`; index avg `-0.131` n `27`; metal avg `0.0171` n `20`; unknown avg `15.4204` n `818`
- 4h: commodity avg `0.3563` n `12`; crypto_alt avg `-1.581` n `233`; crypto_major avg `-1.1177` n `8`; equity avg `-0.5276` n `136`; fx avg `0.0361` n `6`; index avg `-0.1685` n `27`; metal avg `-0.038` n `20`; unknown avg `15.5485` n `788`
- 24h: commodity avg `0.6831` n `12`; crypto_alt avg `-1.7331` n `233`; crypto_major avg `-1.636` n `8`; equity avg `-1.6927` n `136`; fx avg `0.0552` n `6`; index avg `-0.4065` n `26`; metal avg `-0.1131` n `20`; unknown avg `1.6136` n `696`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
