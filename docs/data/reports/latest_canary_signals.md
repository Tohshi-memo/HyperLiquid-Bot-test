# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T12:22:17.595372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0425` n `12`; crypto_alt avg `-0.3531` n `228`; crypto_major avg `-0.1731` n `8`; equity avg `-0.0024` n `67`; fx avg `0.0007` n `6`; index avg `-0.0055` n `23`; metal avg `-0.039` n `18`; unknown avg `-0.1263` n `396`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.4775` n `228`; crypto_major avg `-0.2626` n `8`; equity avg `0.0569` n `67`; fx avg `-0.0253` n `6`; index avg `0.059` n `23`; metal avg `-0.0636` n `18`; unknown avg `0.1967` n `396`
- 4h: commodity avg `0.2018` n `12`; crypto_alt avg `-0.4898` n `228`; crypto_major avg `0.2535` n `8`; equity avg `0.153` n `67`; fx avg `-0.011` n `6`; index avg `-0.0239` n `23`; metal avg `-0.1046` n `18`; unknown avg `-0.3304` n `396`
- 24h: commodity avg `-2.5683` n `12`; crypto_alt avg `3.5234` n `228`; crypto_major avg `4.5257` n `8`; equity avg `2.7469` n `67`; fx avg `0.0526` n `6`; index avg `1.2883` n `23`; metal avg `1.2499` n `18`; unknown avg `1.4479` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
