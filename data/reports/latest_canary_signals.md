# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T09:52:29.814298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0629` n `12`; crypto_alt avg `-0.246` n `234`; crypto_major avg `-0.4005` n `8`; equity avg `-0.0779` n `137`; fx avg `0.0016` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0156` n `20`; unknown avg `0.7325` n `921`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.2273` n `234`; crypto_major avg `-0.1638` n `8`; equity avg `0.0233` n `137`; fx avg `0.0151` n `6`; index avg `0.0303` n `27`; metal avg `0.038` n `20`; unknown avg `-0.0019` n `919`
- 4h: commodity avg `-0.0884` n `12`; crypto_alt avg `0.4959` n `234`; crypto_major avg `0.2966` n `8`; equity avg `0.7806` n `137`; fx avg `0.0583` n `6`; index avg `0.1353` n `27`; metal avg `0.0426` n `20`; unknown avg `-0.0771` n `891`
- 24h: commodity avg `-0.5518` n `12`; crypto_alt avg `3.142` n `234`; crypto_major avg `1.5653` n `8`; equity avg `1.4071` n `137`; fx avg `0.0966` n `6`; index avg `0.1141` n `27`; metal avg `-0.123` n `20`; unknown avg `0.6169` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
