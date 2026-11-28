# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T16:07:27.054552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `-0.1635` n `239`; crypto_major avg `-0.1014` n `8`; equity avg `-0.0577` n `168`; fx avg `0.0096` n `6`; index avg `-0.0014` n `27`; metal avg `0.0043` n `20`; unknown avg `-0.0114` n `1239`
- 1h: commodity avg `-0.0069` n `13`; crypto_alt avg `-0.2964` n `239`; crypto_major avg `0.0824` n `8`; equity avg `-0.0332` n `168`; fx avg `0.0105` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0124` n `20`; unknown avg `0.3208` n `1243`
- 4h: commodity avg `-0.0088` n `13`; crypto_alt avg `-0.8925` n `239`; crypto_major avg `-0.1094` n `8`; equity avg `-0.1577` n `168`; fx avg `0.011` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0329` n `20`; unknown avg `162.5323` n `1233`
- 24h: commodity avg `-0.1573` n `13`; crypto_alt avg `-2.7497` n `239`; crypto_major avg `-1.2904` n `8`; equity avg `0.4223` n `168`; fx avg `-0.0295` n `6`; index avg `0.0326` n `27`; metal avg `0.3201` n `20`; unknown avg `200.2166` n `1082`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
