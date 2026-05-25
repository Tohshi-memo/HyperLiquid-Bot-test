# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T12:07:18.004830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1252` n `12`; crypto_alt avg `-0.1163` n `228`; crypto_major avg `-0.0537` n `8`; equity avg `-0.0026` n `67`; fx avg `-0.0005` n `6`; index avg `0.0362` n `23`; metal avg `-0.1877` n `18`; unknown avg `0.1287` n `405`
- 1h: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.4272` n `228`; crypto_major avg `-0.0511` n `8`; equity avg `0.0634` n `67`; fx avg `0.0037` n `6`; index avg `0.0662` n `23`; metal avg `-0.1105` n `18`; unknown avg `-0.0547` n `397`
- 4h: commodity avg `-0.11` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `-0.0622` n `8`; equity avg `0.2459` n `67`; fx avg `0.0162` n `6`; index avg `0.1492` n `23`; metal avg `0.076` n `18`; unknown avg `-0.3258` n `397`
- 24h: commodity avg `-0.0987` n `12`; crypto_alt avg `0.3621` n `228`; crypto_major avg `-0.1181` n `8`; equity avg `0.586` n `67`; fx avg `0.0367` n `6`; index avg `0.0724` n `23`; metal avg `0.5607` n `18`; unknown avg `0.4437` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
