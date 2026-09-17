# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T09:37:31.561375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `-0.0182` n `234`; crypto_major avg `-0.0507` n `8`; equity avg `0.0243` n `137`; fx avg `0.0139` n `6`; index avg `0.005` n `27`; metal avg `-0.0113` n `20`; unknown avg `0.8779` n `921`
- 1h: commodity avg `0.026` n `12`; crypto_alt avg `0.136` n `234`; crypto_major avg `0.2562` n `8`; equity avg `0.1917` n `137`; fx avg `-0.0047` n `6`; index avg `0.0437` n `27`; metal avg `-0.0715` n `20`; unknown avg `1.2672` n `919`
- 4h: commodity avg `-0.0829` n `12`; crypto_alt avg `0.796` n `234`; crypto_major avg `0.8021` n `8`; equity avg `0.8482` n `137`; fx avg `0.0295` n `6`; index avg `0.139` n `27`; metal avg `0.0773` n `20`; unknown avg `1.086` n `891`
- 24h: commodity avg `-0.4658` n `12`; crypto_alt avg `3.498` n `234`; crypto_major avg `2.0115` n `8`; equity avg `1.5339` n `137`; fx avg `0.0812` n `6`; index avg `0.1324` n `27`; metal avg `-0.1013` n `20`; unknown avg `1.1864` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
