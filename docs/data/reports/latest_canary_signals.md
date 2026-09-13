# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T05:07:28.736308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `12`; crypto_alt avg `0.0677` n `233`; crypto_major avg `0.0711` n `8`; equity avg `-0.0114` n `136`; fx avg `-0.0086` n `6`; index avg `-0.0038` n `26`; metal avg `0.0028` n `20`; unknown avg `0.3674` n `836`
- 1h: commodity avg `0.0311` n `12`; crypto_alt avg `0.0285` n `233`; crypto_major avg `0.0496` n `8`; equity avg `-0.0284` n `136`; fx avg `-0.0071` n `6`; index avg `-0.0113` n `26`; metal avg `0.0004` n `20`; unknown avg `0.9177` n `830`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1643` n `233`; crypto_major avg `-0.1375` n `8`; equity avg `-0.2107` n `136`; fx avg `-0.0014` n `6`; index avg `-0.0424` n `26`; metal avg `0.0045` n `20`; unknown avg `-0.0541` n `806`
- 24h: commodity avg `0.0834` n `12`; crypto_alt avg `1.1428` n `233`; crypto_major avg `0.1786` n `8`; equity avg `-0.558` n `136`; fx avg `-0.0137` n `6`; index avg `-0.069` n `26`; metal avg `0.0349` n `20`; unknown avg `-0.1682` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
