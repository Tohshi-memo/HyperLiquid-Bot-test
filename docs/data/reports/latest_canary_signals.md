# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T05:37:30.662584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.03` n `239`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0812` n `162`; fx avg `0.0164` n `6`; index avg `-0.0159` n `27`; metal avg `0.0518` n `20`; unknown avg `-0.4451` n `1262`
- 1h: commodity avg `-0.0329` n `13`; crypto_alt avg `0.1441` n `239`; crypto_major avg `0.1451` n `8`; equity avg `-0.1331` n `162`; fx avg `0.0125` n `6`; index avg `-0.0168` n `27`; metal avg `0.144` n `20`; unknown avg `-0.6183` n `1256`
- 4h: commodity avg `-0.1072` n `13`; crypto_alt avg `1.0742` n `239`; crypto_major avg `0.9154` n `8`; equity avg `0.0029` n `162`; fx avg `-0.025` n `6`; index avg `-0.0391` n `27`; metal avg `0.2624` n `20`; unknown avg `-0.6585` n `1238`
- 24h: commodity avg `-1.1655` n `13`; crypto_alt avg `1.0448` n `239`; crypto_major avg `1.4781` n `8`; equity avg `-2.2415` n `162`; fx avg `-0.0157` n `6`; index avg `-0.2261` n `27`; metal avg `0.0474` n `20`; unknown avg `562.5422` n `981`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
