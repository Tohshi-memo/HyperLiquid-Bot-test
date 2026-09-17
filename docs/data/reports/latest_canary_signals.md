# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T07:22:30.953208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0794` n `234`; crypto_major avg `0.0533` n `8`; equity avg `0.1187` n `137`; fx avg `-0.0054` n `6`; index avg `0.0054` n `27`; metal avg `0.0387` n `20`; unknown avg `0.0575` n `921`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `0.4995` n `234`; crypto_major avg `0.4418` n `8`; equity avg `0.5135` n `137`; fx avg `0.0074` n `6`; index avg `0.0959` n `27`; metal avg `0.0999` n `20`; unknown avg `-0.098` n `919`
- 4h: commodity avg `-0.2411` n `12`; crypto_alt avg `0.9915` n `234`; crypto_major avg `0.273` n `8`; equity avg `0.4462` n `137`; fx avg `0.013` n `6`; index avg `0.0715` n `27`; metal avg `0.2133` n `20`; unknown avg `-0.059` n `891`
- 24h: commodity avg `-0.5483` n `12`; crypto_alt avg `3.1746` n `234`; crypto_major avg `1.6576` n `8`; equity avg `1.1668` n `137`; fx avg `0.0619` n `6`; index avg `0.1001` n `27`; metal avg `-0.119` n `20`; unknown avg `0.3006` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
