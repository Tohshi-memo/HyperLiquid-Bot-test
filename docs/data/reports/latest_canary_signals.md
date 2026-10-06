# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T18:52:48.641071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1333` n `13`; crypto_alt avg `0.0747` n `235`; crypto_major avg `0.0256` n `8`; equity avg `0.0057` n `150`; fx avg `0.0047` n `6`; index avg `0.0032` n `26`; metal avg `0.0405` n `20`; unknown avg `2.0712` n `1076`
- 1h: commodity avg `0.2124` n `13`; crypto_alt avg `-0.0965` n `235`; crypto_major avg `-0.0512` n `8`; equity avg `-0.2012` n `150`; fx avg `-0.0115` n `6`; index avg `-0.0279` n `26`; metal avg `0.0554` n `20`; unknown avg `2.5458` n `1074`
- 4h: commodity avg `0.5884` n `13`; crypto_alt avg `-0.7441` n `235`; crypto_major avg `-0.8646` n `8`; equity avg `-0.2347` n `150`; fx avg `0.0129` n `6`; index avg `-0.0732` n `26`; metal avg `0.2459` n `20`; unknown avg `3.12` n `1064`
- 24h: commodity avg `0.2623` n `13`; crypto_alt avg `-0.1978` n `235`; crypto_major avg `-0.2183` n `8`; equity avg `0.6727` n `149`; fx avg `0.1124` n `6`; index avg `0.0248` n `26`; metal avg `0.0597` n `20`; unknown avg `383.6438` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
