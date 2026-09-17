# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T07:37:38.136940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.0375` n `234`; crypto_major avg `-0.0476` n `8`; equity avg `0.0272` n `137`; fx avg `0.01` n `6`; index avg `0.0115` n `27`; metal avg `0.0997` n `20`; unknown avg `1.7025` n `921`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `0.2176` n `234`; crypto_major avg `0.1396` n `8`; equity avg `0.3552` n `137`; fx avg `0.0126` n `6`; index avg `0.0597` n `27`; metal avg `0.1902` n `20`; unknown avg `1.1548` n `919`
- 4h: commodity avg `-0.1629` n `12`; crypto_alt avg `0.6938` n `234`; crypto_major avg `0.0595` n `8`; equity avg `0.43` n `137`; fx avg `0.0174` n `6`; index avg `0.072` n `27`; metal avg `0.2524` n `20`; unknown avg `1.1754` n `891`
- 24h: commodity avg `-0.4915` n `12`; crypto_alt avg `3.1487` n `234`; crypto_major avg `1.6378` n `8`; equity avg `1.1924` n `137`; fx avg `0.0718` n `6`; index avg `0.1074` n `27`; metal avg `-0.0539` n `20`; unknown avg `1.0297` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
