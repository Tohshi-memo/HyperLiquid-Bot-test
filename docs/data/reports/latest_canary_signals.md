# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T17:22:30.426140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.0738` n `235`; crypto_major avg `0.0591` n `8`; equity avg `-0.0589` n `151`; fx avg `0.006` n `6`; index avg `-0.0102` n `26`; metal avg `0.0169` n `20`; unknown avg `0.7981` n `1135`
- 1h: commodity avg `0.1113` n `13`; crypto_alt avg `-0.1885` n `235`; crypto_major avg `-0.2674` n `8`; equity avg `-0.1757` n `151`; fx avg `-0.01` n `6`; index avg `0.0001` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0653` n `1133`
- 4h: commodity avg `0.602` n `13`; crypto_alt avg `-0.0279` n `235`; crypto_major avg `0.1297` n `8`; equity avg `0.5809` n `151`; fx avg `-0.0121` n `6`; index avg `0.0646` n `26`; metal avg `-0.2432` n `20`; unknown avg `0.2811` n `1095`
- 24h: commodity avg `0.5279` n `13`; crypto_alt avg `-1.4605` n `235`; crypto_major avg `-0.3999` n `8`; equity avg `-1.1376` n `151`; fx avg `0.1353` n `6`; index avg `-0.2121` n `26`; metal avg `-0.2475` n `20`; unknown avg `0.4352` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1621`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1474`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1226`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0911`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.09`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
