# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T03:07:27.507842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `-0.0378` n `228`; crypto_major avg `0.0038` n `8`; equity avg `-0.0191` n `78`; fx avg `0.0088` n `6`; index avg `-0.0005` n `23`; metal avg `-0.0435` n `18`; unknown avg `0.0229` n `687`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `-0.3571` n `228`; crypto_major avg `-0.2277` n `8`; equity avg `0.0873` n `78`; fx avg `0.0095` n `6`; index avg `0.028` n `23`; metal avg `-0.048` n `18`; unknown avg `-0.0845` n `687`
- 4h: commodity avg `0.1323` n `12`; crypto_alt avg `-0.1858` n `228`; crypto_major avg `-0.0694` n `8`; equity avg `0.1384` n `78`; fx avg `0.0478` n `6`; index avg `0.09` n `23`; metal avg `-0.0772` n `18`; unknown avg `-0.5992` n `671`
- 24h: commodity avg `0.4492` n `12`; crypto_alt avg `-3.924` n `228`; crypto_major avg `-4.6137` n `8`; equity avg `0.935` n `78`; fx avg `-0.0751` n `6`; index avg `0.3074` n `23`; metal avg `-4.171` n `18`; unknown avg `-0.5442` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
