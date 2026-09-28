# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T06:22:26.993750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2126` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.4195` n `234`; crypto_major avg `-0.2434` n `8`; equity avg `-0.1282` n `141`; fx avg `0.0028` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0358` n `20`; unknown avg `2.3549` n `962`
- 1h: commodity avg `-0.0602` n `12`; crypto_alt avg `-0.3323` n `234`; crypto_major avg `-0.3914` n `8`; equity avg `-0.1295` n `141`; fx avg `0.0108` n `6`; index avg `-0.0308` n `26`; metal avg `-0.0181` n `20`; unknown avg `3.1464` n `936`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `-2.1247` n `234`; crypto_major avg `-1.2653` n `8`; equity avg `-0.5072` n `141`; fx avg `0.0186` n `6`; index avg `-0.0527` n `26`; metal avg `-0.2504` n `20`; unknown avg `0.8411` n `926`
- 24h: commodity avg `-0.3814` n `12`; crypto_alt avg `-2.5842` n `234`; crypto_major avg `-2.4129` n `8`; equity avg `-1.7253` n `141`; fx avg `0.0906` n `6`; index avg `-0.1922` n `26`; metal avg `-0.7962` n `20`; unknown avg `3.902` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
