# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T23:54:18.134639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0544` n `12`; crypto_alt avg `-0.2406` n `228`; crypto_major avg `-0.1206` n `8`; equity avg `0.1221` n `67`; fx avg `0.0145` n `6`; index avg `0.0988` n `23`; metal avg `0.1246` n `18`; unknown avg `-0.0193` n `418`
- 1h: commodity avg `-0.1151` n `12`; crypto_alt avg `0.0015` n `228`; crypto_major avg `0.096` n `8`; equity avg `0.1268` n `67`; fx avg `0.0005` n `6`; index avg `0.1756` n `23`; metal avg `0.2771` n `18`; unknown avg `-0.1973` n `418`
- 4h: commodity avg `-0.1149` n `12`; crypto_alt avg `-0.3842` n `228`; crypto_major avg `-0.5012` n `8`; equity avg `0.2281` n `67`; fx avg `0.0229` n `6`; index avg `0.082` n `23`; metal avg `0.3629` n `18`; unknown avg `-0.5746` n `418`
- 24h: commodity avg `0.5596` n `12`; crypto_alt avg `-1.633` n `228`; crypto_major avg `-1.5016` n `8`; equity avg `0.0529` n `67`; fx avg `-0.098` n `6`; index avg `0.7977` n `23`; metal avg `-0.277` n `18`; unknown avg `0.1471` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
