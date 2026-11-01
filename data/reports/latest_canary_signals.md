# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T23:52:28.840995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.0492` n `238`; crypto_major avg `0.1616` n `8`; equity avg `0.1399` n `156`; fx avg `-0.0146` n `6`; index avg `0.0352` n `27`; metal avg `0.0426` n `20`; unknown avg `0.4748` n `1263`
- 1h: commodity avg `-0.0756` n `13`; crypto_alt avg `0.5061` n `238`; crypto_major avg `0.5761` n `8`; equity avg `0.2598` n `156`; fx avg `0.0059` n `6`; index avg `0.0307` n `27`; metal avg `0.1484` n `20`; unknown avg `159.8185` n `1255`
- 4h: commodity avg `-0.0534` n `13`; crypto_alt avg `0.4858` n `238`; crypto_major avg `0.6135` n `8`; equity avg `0.3113` n `156`; fx avg `-0.0003` n `6`; index avg `0.0409` n `27`; metal avg `0.1526` n `20`; unknown avg `302.9013` n `1205`
- 24h: commodity avg `-0.0324` n `13`; crypto_alt avg `-0.217` n `238`; crypto_major avg `0.3254` n `8`; equity avg `0.5358` n `156`; fx avg `0.0005` n `6`; index avg `0.0771` n `27`; metal avg `0.173` n `20`; unknown avg `3.5258` n `1084`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
