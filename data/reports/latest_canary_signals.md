# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T09:37:28.873310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.1123` n `232`; crypto_major avg `-0.1064` n `8`; equity avg `-0.0601` n `128`; fx avg `0.0059` n `6`; index avg `-0.012` n `26`; metal avg `-0.0097` n `20`; unknown avg `-0.0489` n `793`
- 1h: commodity avg `0.0647` n `12`; crypto_alt avg `0.0408` n `232`; crypto_major avg `0.2992` n `8`; equity avg `-0.0554` n `128`; fx avg `0.0062` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0053` n `20`; unknown avg `0.3688` n `791`
- 4h: commodity avg `0.0289` n `12`; crypto_alt avg `0.2168` n `232`; crypto_major avg `0.552` n `8`; equity avg `0.3031` n `128`; fx avg `-0.0762` n `6`; index avg `0.079` n `26`; metal avg `0.0634` n `20`; unknown avg `0.4284` n `773`
- 24h: commodity avg `0.5715` n `12`; crypto_alt avg `0.0747` n `231`; crypto_major avg `-0.8805` n `8`; equity avg `-0.3054` n `128`; fx avg `-0.1267` n `6`; index avg `-0.0496` n `26`; metal avg `-0.2296` n `20`; unknown avg `-0.3239` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
