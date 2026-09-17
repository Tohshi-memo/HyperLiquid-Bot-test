# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T04:52:31.994420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0367` n `12`; crypto_alt avg `0.366` n `234`; crypto_major avg `0.2827` n `8`; equity avg `0.0656` n `137`; fx avg `0.0094` n `6`; index avg `0.0168` n `27`; metal avg `0.0221` n `20`; unknown avg `0.9091` n `921`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.2976` n `234`; crypto_major avg `0.0057` n `8`; equity avg `0.0843` n `137`; fx avg `0.0097` n `6`; index avg `0.0136` n `27`; metal avg `0.012` n `20`; unknown avg `0.0499` n `913`
- 4h: commodity avg `0.2477` n `12`; crypto_alt avg `0.8548` n `234`; crypto_major avg `0.465` n `8`; equity avg `0.2811` n `137`; fx avg `0.042` n `6`; index avg `0.0399` n `27`; metal avg `0.2649` n `20`; unknown avg `-0.4382` n `911`
- 24h: commodity avg `-0.4` n `12`; crypto_alt avg `2.2486` n `234`; crypto_major avg `1.2747` n `8`; equity avg `1.2368` n `137`; fx avg `0.0385` n `6`; index avg `0.122` n `27`; metal avg `-0.1736` n `20`; unknown avg `0.7786` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
