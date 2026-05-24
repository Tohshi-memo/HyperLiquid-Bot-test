# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T19:37:15.925272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0546` n `12`; crypto_alt avg `-0.1204` n `228`; crypto_major avg `-0.0779` n `8`; equity avg `-0.0098` n `67`; fx avg `-0.0057` n `6`; index avg `-0.0088` n `23`; metal avg `-0.0098` n `18`; unknown avg `-0.0973` n `396`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `-0.1644` n `228`; crypto_major avg `0.0523` n `8`; equity avg `-0.0172` n `67`; fx avg `0.0085` n `6`; index avg `0.0138` n `23`; metal avg `-0.0746` n `18`; unknown avg `-0.3013` n `396`
- 4h: commodity avg `0.2279` n `12`; crypto_alt avg `0.0471` n `228`; crypto_major avg `0.021` n `8`; equity avg `0.1107` n `67`; fx avg `0.0183` n `6`; index avg `0.0914` n `23`; metal avg `-0.0631` n `18`; unknown avg `-0.6754` n `396`
- 24h: commodity avg `-0.295` n `12`; crypto_alt avg `-0.6969` n `228`; crypto_major avg `1.4673` n `8`; equity avg `1.1189` n `67`; fx avg `0.0975` n `6`; index avg `0.339` n `23`; metal avg `0.376` n `18`; unknown avg `0.4057` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
