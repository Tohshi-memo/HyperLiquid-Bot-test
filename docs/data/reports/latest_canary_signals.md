# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T18:07:30.692180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `0.1776` n `234`; crypto_major avg `0.1974` n `8`; equity avg `-0.0086` n `141`; fx avg `0.0004` n `6`; index avg `0.005` n `26`; metal avg `0.0007` n `20`; unknown avg `2.806` n `958`
- 1h: commodity avg `0.2138` n `12`; crypto_alt avg `-0.0492` n `234`; crypto_major avg `-0.0532` n `8`; equity avg `-0.1092` n `141`; fx avg `-0.0119` n `6`; index avg `0.0073` n `26`; metal avg `-0.033` n `20`; unknown avg `1.2938` n `958`
- 4h: commodity avg `-0.1577` n `12`; crypto_alt avg `1.1156` n `234`; crypto_major avg `0.2936` n `8`; equity avg `0.3138` n `141`; fx avg `-0.0165` n `6`; index avg `0.1225` n `26`; metal avg `0.2861` n `20`; unknown avg `0.4498` n `930`
- 24h: commodity avg `-0.7612` n `12`; crypto_alt avg `2.2994` n `234`; crypto_major avg `0.8943` n `8`; equity avg `0.4487` n `141`; fx avg `-0.2602` n `6`; index avg `0.2478` n `26`; metal avg `0.1901` n `20`; unknown avg `1599.4407` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
