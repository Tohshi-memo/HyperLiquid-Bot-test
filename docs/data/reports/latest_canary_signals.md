# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T16:17:09.342779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.0954` n `231`; crypto_major avg `-0.151` n `8`; equity avg `-0.0711` n `122`; fx avg `-0.0102` n `6`; index avg `0.0002` n `25`; metal avg `-0.0088` n `20`; unknown avg `-0.0393` n `795`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `0.1749` n `231`; crypto_major avg `0.1021` n `8`; equity avg `0.1459` n `122`; fx avg `-0.0205` n `6`; index avg `0.0326` n `25`; metal avg `0.0681` n `20`; unknown avg `0.0701` n `795`
- 4h: commodity avg `-0.038` n `12`; crypto_alt avg `0.1783` n `231`; crypto_major avg `0.494` n `8`; equity avg `0.4194` n `122`; fx avg `0.0172` n `6`; index avg `-0.0661` n `25`; metal avg `0.1796` n `20`; unknown avg `0.0696` n `795`
- 24h: commodity avg `-0.6965` n `12`; crypto_alt avg `-1.6464` n `231`; crypto_major avg `-0.8116` n `8`; equity avg `1.3414` n `122`; fx avg `0.0352` n `6`; index avg `0.1651` n `25`; metal avg `-0.1627` n `20`; unknown avg `-0.961` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
