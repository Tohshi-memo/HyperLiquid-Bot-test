# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T11:22:16.518330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `-0.1424` n `228`; crypto_major avg `-0.0303` n `8`; equity avg `-0.0957` n `67`; fx avg `0.0127` n `6`; index avg `-0.0871` n `23`; metal avg `0.0059` n `18`; unknown avg `0.0234` n `396`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0867` n `228`; crypto_major avg `0.1491` n `8`; equity avg `-0.0044` n `67`; fx avg `0.0147` n `6`; index avg `-0.0775` n `23`; metal avg `-0.0417` n `18`; unknown avg `0.2438` n `396`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.023` n `228`; crypto_major avg `0.5919` n `8`; equity avg `0.0959` n `67`; fx avg `0.0137` n `6`; index avg `-0.1107` n `23`; metal avg `0.0888` n `18`; unknown avg `-0.1448` n `396`
- 24h: commodity avg `-2.6922` n `12`; crypto_alt avg `3.62` n `228`; crypto_major avg `4.5952` n `8`; equity avg `2.6616` n `67`; fx avg `0.0732` n `6`; index avg `1.3069` n `23`; metal avg `1.3214` n `18`; unknown avg `1.4936` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
