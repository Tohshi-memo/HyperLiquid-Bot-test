# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T12:22:23.935628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0731` n `12`; crypto_alt avg `0.4917` n `234`; crypto_major avg `0.7058` n `8`; equity avg `0.2421` n `137`; fx avg `-0.0439` n `6`; index avg `0.0595` n `27`; metal avg `0.2044` n `20`; unknown avg `1.1445` n `921`
- 1h: commodity avg `-0.2032` n `12`; crypto_alt avg `0.5566` n `234`; crypto_major avg `0.8174` n `8`; equity avg `0.3584` n `137`; fx avg `-0.0441` n `6`; index avg `0.1119` n `27`; metal avg `0.2622` n `20`; unknown avg `0.336` n `919`
- 4h: commodity avg `-0.4215` n `12`; crypto_alt avg `0.4573` n `234`; crypto_major avg `0.5142` n `8`; equity avg `0.6841` n `137`; fx avg `-0.1081` n `6`; index avg `0.2223` n `27`; metal avg `0.338` n `20`; unknown avg `0.5473` n `911`
- 24h: commodity avg `-0.8385` n `12`; crypto_alt avg `3.5269` n `234`; crypto_major avg `1.8604` n `8`; equity avg `1.5512` n `137`; fx avg `0.0323` n `6`; index avg `0.2057` n `27`; metal avg `0.2598` n `20`; unknown avg `0.3143` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
