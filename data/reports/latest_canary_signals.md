# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T04:52:24.647840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.181` n `234`; crypto_major avg `0.1845` n `8`; equity avg `0.0515` n `140`; fx avg `0.0005` n `6`; index avg `-0.0003` n `26`; metal avg `0.0005` n `20`; unknown avg `0.1544` n `944`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `0.1571` n `234`; crypto_major avg `0.0615` n `8`; equity avg `-0.0313` n `140`; fx avg `0.0319` n `6`; index avg `0.003` n `26`; metal avg `0.0073` n `20`; unknown avg `43.2748` n `936`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `0.5125` n `234`; crypto_major avg `-0.5462` n `8`; equity avg `-0.0124` n `140`; fx avg `-0.0034` n `6`; index avg `0.045` n `26`; metal avg `0.0148` n `20`; unknown avg `44.7051` n `935`
- 24h: commodity avg `-0.6027` n `12`; crypto_alt avg `3.6827` n `234`; crypto_major avg `2.6255` n `8`; equity avg `1.1514` n `140`; fx avg `0.0011` n `6`; index avg `0.2221` n `26`; metal avg `0.0524` n `20`; unknown avg `4.2343` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
