# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T05:37:25.935898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0595` n `12`; crypto_alt avg `-0.1003` n `232`; crypto_major avg `-0.1133` n `8`; equity avg `-0.0632` n `128`; fx avg `-0.0029` n `6`; index avg `-0.031` n `26`; metal avg `-0.0007` n `20`; unknown avg `8.0916` n `793`
- 1h: commodity avg `0.1322` n `12`; crypto_alt avg `0.6898` n `232`; crypto_major avg `0.5898` n `8`; equity avg `0.514` n `128`; fx avg `0.0036` n `6`; index avg `0.0656` n `26`; metal avg `0.0751` n `20`; unknown avg `0.7643` n `791`
- 4h: commodity avg `0.1763` n `12`; crypto_alt avg `0.9407` n `231`; crypto_major avg `0.408` n `8`; equity avg `0.6565` n `128`; fx avg `-0.0128` n `6`; index avg `0.1654` n `26`; metal avg `0.0158` n `20`; unknown avg `-0.11` n `779`
- 24h: commodity avg `0.5299` n `12`; crypto_alt avg `-0.1266` n `231`; crypto_major avg `-1.5889` n `8`; equity avg `-0.6003` n `128`; fx avg `-0.0456` n `6`; index avg `-0.1447` n `26`; metal avg `-0.2896` n `20`; unknown avg `-0.4607` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
