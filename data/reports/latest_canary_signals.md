# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T23:37:29.148336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.1944` n `232`; crypto_major avg `0.0643` n `8`; equity avg `0.0046` n `134`; fx avg `0.0107` n `6`; index avg `-0.008` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.1645` n `790`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `0.4513` n `232`; crypto_major avg `0.1688` n `8`; equity avg `0.018` n `134`; fx avg `0.0168` n `6`; index avg `-0.022` n `26`; metal avg `-0.0101` n `20`; unknown avg `448.5336` n `790`
- 4h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.0433` n `232`; crypto_major avg `-0.0022` n `8`; equity avg `0.1675` n `134`; fx avg `0.0075` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.2235` n `748`
- 24h: commodity avg `-0.0015` n `12`; crypto_alt avg `-1.0921` n `232`; crypto_major avg `-2.1447` n `8`; equity avg `1.662` n `133`; fx avg `-0.0937` n `6`; index avg `0.1612` n `26`; metal avg `-0.2718` n `20`; unknown avg `0.8137` n `668`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
