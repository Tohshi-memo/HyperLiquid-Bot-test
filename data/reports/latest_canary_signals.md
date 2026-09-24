# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T00:52:33.637551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.2281` n `234`; crypto_major avg `-0.2326` n `8`; equity avg `-0.1983` n `141`; fx avg `0.079` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.0914` n `945`
- 1h: commodity avg `-0.0448` n `12`; crypto_alt avg `-0.1499` n `234`; crypto_major avg `-0.1102` n `8`; equity avg `-0.2476` n `141`; fx avg `0.0919` n `6`; index avg `-0.0186` n `26`; metal avg `-0.045` n `20`; unknown avg `-0.0857` n `937`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.3496` n `234`; crypto_major avg `0.4951` n `8`; equity avg `-0.1921` n `141`; fx avg `0.0798` n `6`; index avg `-0.0428` n `26`; metal avg `-0.0576` n `20`; unknown avg `-0.4419` n `921`
- 24h: commodity avg `0.3741` n `12`; crypto_alt avg `-4.6441` n `234`; crypto_major avg `-3.7515` n `8`; equity avg `-1.8677` n `140`; fx avg `0.141` n `6`; index avg `-0.3484` n `26`; metal avg `-0.8769` n `20`; unknown avg `583.2703` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
