# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T23:37:27.271319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `0.0223` n `239`; crypto_major avg `0.0689` n `8`; equity avg `-0.0027` n `166`; fx avg `0.0005` n `6`; index avg `0.0204` n `27`; metal avg `0.006` n `20`; unknown avg `0.2956` n `1266`
- 1h: commodity avg `-0.0042` n `13`; crypto_alt avg `0.1645` n `239`; crypto_major avg `0.1539` n `8`; equity avg `0.0115` n `166`; fx avg `0.0073` n `6`; index avg `0.0398` n `27`; metal avg `0.0151` n `20`; unknown avg `162.7278` n `1242`
- 4h: commodity avg `-0.004` n `13`; crypto_alt avg `0.1138` n `239`; crypto_major avg `-0.2564` n `8`; equity avg `0.1004` n `166`; fx avg `0.015` n `6`; index avg `0.0513` n `27`; metal avg `-0.0748` n `20`; unknown avg `41.2798` n `1196`
- 24h: commodity avg `0.0121` n `13`; crypto_alt avg `-0.1046` n `239`; crypto_major avg `1.5932` n `8`; equity avg `0.2982` n `166`; fx avg `-0.0243` n `6`; index avg `0.154` n `27`; metal avg `0.087` n `20`; unknown avg `231.6506` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
