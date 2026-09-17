# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T02:22:29.770584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.2962` n `234`; crypto_major avg `-0.2002` n `8`; equity avg `-0.0959` n `137`; fx avg `-0.013` n `6`; index avg `-0.0047` n `27`; metal avg `0.002` n `20`; unknown avg `0.076` n `919`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.1906` n `234`; crypto_major avg `-0.1572` n `8`; equity avg `-0.2502` n `137`; fx avg `0.0204` n `6`; index avg `-0.0543` n `27`; metal avg `-0.1085` n `20`; unknown avg `0.1476` n `917`
- 4h: commodity avg `0.0642` n `12`; crypto_alt avg `1.3386` n `234`; crypto_major avg `0.702` n `8`; equity avg `0.3405` n `137`; fx avg `0.0313` n `6`; index avg `0.093` n `27`; metal avg `0.2305` n `20`; unknown avg `0.6897` n `869`
- 24h: commodity avg `-0.4699` n `12`; crypto_alt avg `1.6697` n `234`; crypto_major avg `0.9391` n `8`; equity avg `1.4427` n `137`; fx avg `0.0048` n `6`; index avg `0.1392` n `27`; metal avg `-0.0944` n `20`; unknown avg `0.5085` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
