# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T09:37:22.193467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2677` n `12`; crypto_alt avg `0.0062` n `228`; crypto_major avg `0.0827` n `8`; equity avg `0.0881` n `67`; fx avg `0.0041` n `6`; index avg `0.014` n `23`; metal avg `-0.0487` n `18`; unknown avg `-0.1805` n `418`
- 1h: commodity avg `0.046` n `12`; crypto_alt avg `-0.6265` n `228`; crypto_major avg `-0.1037` n `8`; equity avg `0.0234` n `67`; fx avg `-0.0273` n `6`; index avg `-0.0385` n `23`; metal avg `0.1432` n `18`; unknown avg `-0.0836` n `418`
- 4h: commodity avg `-0.7168` n `12`; crypto_alt avg `0.0943` n `228`; crypto_major avg `0.4166` n `8`; equity avg `0.5697` n `67`; fx avg `-0.0078` n `6`; index avg `0.0724` n `23`; metal avg `-0.3371` n `18`; unknown avg `-0.0228` n `400`
- 24h: commodity avg `-1.7051` n `12`; crypto_alt avg `-1.0845` n `228`; crypto_major avg `0.3909` n `8`; equity avg `0.8709` n `67`; fx avg `-0.0782` n `6`; index avg `0.8048` n `23`; metal avg `-0.3063` n `18`; unknown avg `0.7714` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
