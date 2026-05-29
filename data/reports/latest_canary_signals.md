# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T21:37:24.534864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.073` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1277` n `12`; crypto_alt avg `-0.314` n `228`; crypto_major avg `-0.2336` n `8`; equity avg `0.0605` n `69`; fx avg `-0.0075` n `6`; index avg `-0.0398` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.0067` n `419`
- 1h: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.4996` n `228`; crypto_major avg `-0.4588` n `8`; equity avg `0.0308` n `69`; fx avg `-0.0287` n `6`; index avg `-0.0926` n `23`; metal avg `-0.1214` n `18`; unknown avg `0.1509` n `419`
- 4h: commodity avg `0.1719` n `12`; crypto_alt avg `-1.3798` n `228`; crypto_major avg `-1.1846` n `8`; equity avg `-0.051` n `69`; fx avg `-0.0219` n `6`; index avg `-0.1116` n `23`; metal avg `-0.173` n `18`; unknown avg `-0.209` n `419`
- 24h: commodity avg `-0.4284` n `12`; crypto_alt avg `-0.0949` n `228`; crypto_major avg `0.2576` n `8`; equity avg `1.2545` n `69`; fx avg `0.1837` n `6`; index avg `0.0534` n `23`; metal avg `0.0014` n `18`; unknown avg `0.3854` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
