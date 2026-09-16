# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T12:22:32.463256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `-0.2973` n `234`; crypto_major avg `-0.2118` n `8`; equity avg `-0.0072` n `137`; fx avg `-0.0035` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0778` n `20`; unknown avg `0.8344` n `919`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `0.0075` n `234`; crypto_major avg `0.1221` n `8`; equity avg `0.2397` n `137`; fx avg `-0.0226` n `6`; index avg `0.0624` n `27`; metal avg `-0.0741` n `20`; unknown avg `10.5554` n `917`
- 4h: commodity avg `0.0331` n `12`; crypto_alt avg `0.556` n `234`; crypto_major avg `0.8085` n `8`; equity avg `0.42` n `137`; fx avg `-0.0268` n `6`; index avg `0.088` n `27`; metal avg `0.0151` n `20`; unknown avg `0.3444` n `911`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `-2.8851` n `234`; crypto_major avg `-2.562` n `8`; equity avg `0.0116` n `137`; fx avg `0.0606` n `6`; index avg `0.0888` n `27`; metal avg `0.4794` n `20`; unknown avg `18892.1652` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
