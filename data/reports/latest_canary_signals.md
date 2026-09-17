# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T04:22:28.226265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.1016` n `234`; crypto_major avg `-0.223` n `8`; equity avg `-0.0387` n `137`; fx avg `0.0004` n `6`; index avg `-0.0098` n `27`; metal avg `-0.0084` n `20`; unknown avg `1.8339` n `921`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0136` n `234`; crypto_major avg `-0.2492` n `8`; equity avg `0.157` n `137`; fx avg `0.0042` n `6`; index avg `0.0323` n `27`; metal avg `0.0823` n `20`; unknown avg `0.0731` n `919`
- 4h: commodity avg `0.1742` n `12`; crypto_alt avg `0.1801` n `234`; crypto_major avg `0.0251` n `8`; equity avg `0.2314` n `137`; fx avg `0.0361` n `6`; index avg `0.0312` n `27`; metal avg `0.1775` n `20`; unknown avg `0.1659` n `911`
- 24h: commodity avg `-0.3322` n `12`; crypto_alt avg `1.5468` n `234`; crypto_major avg `0.7372` n `8`; equity avg `1.0468` n `137`; fx avg `0.033` n `6`; index avg `0.0891` n `27`; metal avg `-0.2329` n `20`; unknown avg `0.5025` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
