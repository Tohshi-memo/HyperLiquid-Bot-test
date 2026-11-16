# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T05:37:34.601723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `-0.3321` n `239`; crypto_major avg `-0.3347` n `8`; equity avg `-0.3799` n `162`; fx avg `-0.0144` n `6`; index avg `-0.0422` n `27`; metal avg `-0.0621` n `20`; unknown avg `0.097` n `1261`
- 1h: commodity avg `0.014` n `13`; crypto_alt avg `-0.4766` n `239`; crypto_major avg `-0.3295` n `8`; equity avg `-0.6004` n `162`; fx avg `-0.0441` n `6`; index avg `-0.0726` n `27`; metal avg `0.0088` n `20`; unknown avg `-0.1578` n `1257`
- 4h: commodity avg `0.0832` n `13`; crypto_alt avg `0.2917` n `239`; crypto_major avg `0.0103` n `8`; equity avg `-0.5839` n `162`; fx avg `-0.0704` n `6`; index avg `-0.0936` n `27`; metal avg `0.025` n `20`; unknown avg `-0.1441` n `1241`
- 24h: commodity avg `-0.361` n `13`; crypto_alt avg `-0.2073` n `239`; crypto_major avg `0.1796` n `8`; equity avg `-0.4065` n `162`; fx avg `-0.0773` n `6`; index avg `-0.0462` n `27`; metal avg `0.2046` n `20`; unknown avg `0.5421` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
