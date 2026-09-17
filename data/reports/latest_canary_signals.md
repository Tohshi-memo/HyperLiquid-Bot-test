# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T09:07:32.585699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `0.0511` n `234`; crypto_major avg `0.1776` n `8`; equity avg `0.1242` n `137`; fx avg `0.0093` n `6`; index avg `0.0411` n `27`; metal avg `0.0386` n `20`; unknown avg `0.6985` n `919`
- 1h: commodity avg `-0.0706` n `12`; crypto_alt avg `0.3709` n `234`; crypto_major avg `0.2876` n `8`; equity avg `0.2777` n `137`; fx avg `0.0134` n `6`; index avg `0.0529` n `27`; metal avg `-0.157` n `20`; unknown avg `1.0121` n `911`
- 4h: commodity avg `-0.1701` n `12`; crypto_alt avg `0.851` n `234`; crypto_major avg `0.5613` n `8`; equity avg `0.6366` n `137`; fx avg `0.0383` n `6`; index avg `0.0838` n `27`; metal avg `0.0356` n `20`; unknown avg `-0.0346` n `891`
- 24h: commodity avg `-0.5844` n `12`; crypto_alt avg `3.7032` n `234`; crypto_major avg `2.1315` n `8`; equity avg `1.5927` n `137`; fx avg `0.0788` n `6`; index avg `0.1186` n `27`; metal avg `-0.1115` n `20`; unknown avg `0.649` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
