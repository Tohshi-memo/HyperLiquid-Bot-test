# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T00:22:16.106173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.104` n `12`; crypto_alt avg `-0.1095` n `228`; crypto_major avg `-0.0209` n `8`; equity avg `-0.0348` n `67`; fx avg `0.0058` n `6`; index avg `-0.0022` n `23`; metal avg `-0.0004` n `18`; unknown avg `-0.1381` n `396`
- 1h: commodity avg `-0.0524` n `12`; crypto_alt avg `-0.0763` n `228`; crypto_major avg `0.0338` n `8`; equity avg `0.0074` n `67`; fx avg `-0.0092` n `6`; index avg `0.1059` n `23`; metal avg `0.117` n `18`; unknown avg `0.207` n `396`
- 4h: commodity avg `-0.9456` n `12`; crypto_alt avg `0.523` n `228`; crypto_major avg `0.5923` n `8`; equity avg `0.7183` n `67`; fx avg `0.0802` n `6`; index avg `0.3237` n `23`; metal avg `0.6093` n `18`; unknown avg `0.2384` n `396`
- 24h: commodity avg `-2.9287` n `12`; crypto_alt avg `2.6567` n `228`; crypto_major avg `2.2652` n `8`; equity avg `1.9891` n `67`; fx avg `0.0538` n `6`; index avg `0.9947` n `23`; metal avg `0.9491` n `18`; unknown avg `0.9579` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
