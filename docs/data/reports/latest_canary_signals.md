# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T20:07:30.849986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0383` n `13`; crypto_alt avg `0.0831` n `239`; crypto_major avg `-0.0181` n `8`; equity avg `0.2331` n `164`; fx avg `0.0028` n `6`; index avg `0.013` n `27`; metal avg `0.0422` n `20`; unknown avg `4.2788` n `1251`
- 1h: commodity avg `0.1271` n `13`; crypto_alt avg `-0.1224` n `239`; crypto_major avg `-0.1868` n `8`; equity avg `0.1206` n `164`; fx avg `-0.0061` n `6`; index avg `0.0121` n `27`; metal avg `-0.024` n `20`; unknown avg `3.6739` n `1255`
- 4h: commodity avg `0.1983` n `13`; crypto_alt avg `-0.0688` n `239`; crypto_major avg `-0.0681` n `8`; equity avg `-0.0244` n `164`; fx avg `0.0088` n `6`; index avg `0.0116` n `27`; metal avg `-0.0366` n `20`; unknown avg `1.0041` n `1253`
- 24h: commodity avg `0.0098` n `13`; crypto_alt avg `-0.0298` n `239`; crypto_major avg `-0.8025` n `8`; equity avg `0.4774` n `164`; fx avg `-0.1742` n `6`; index avg `0.0805` n `27`; metal avg `-1.0774` n `20`; unknown avg `-0.0669` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
