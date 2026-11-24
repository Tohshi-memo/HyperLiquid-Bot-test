# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T21:37:29.728033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `-0.1624` n `239`; crypto_major avg `-0.0366` n `8`; equity avg `-0.0957` n `168`; fx avg `-0.0049` n `6`; index avg `-0.0119` n `27`; metal avg `-0.0118` n `20`; unknown avg `157.7269` n `1265`
- 1h: commodity avg `0.058` n `13`; crypto_alt avg `0.3366` n `239`; crypto_major avg `0.6411` n `8`; equity avg `0.5626` n `168`; fx avg `-0.018` n `6`; index avg `0.0669` n `27`; metal avg `0.0816` n `20`; unknown avg `1.8738` n `1231`
- 4h: commodity avg `-0.0249` n `13`; crypto_alt avg `-0.754` n `239`; crypto_major avg `-0.3369` n `8`; equity avg `-0.1471` n `168`; fx avg `-0.0569` n `6`; index avg `-0.0273` n `27`; metal avg `-0.0195` n `20`; unknown avg `381.2618` n `1201`
- 24h: commodity avg `0.6232` n `13`; crypto_alt avg `-3.142` n `239`; crypto_major avg `-2.748` n `8`; equity avg `-4.0653` n `167`; fx avg `0.2229` n `6`; index avg `-0.2654` n `27`; metal avg `-1.0748` n `20`; unknown avg `409.3467` n `1111`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
