# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T05:07:32.613312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.0693` n `228`; crypto_major avg `-0.0375` n `8`; equity avg `0.0233` n `88`; fx avg `-0.0306` n `6`; index avg `0.0215` n `23`; metal avg `-0.0538` n `20`; unknown avg `-0.4707` n `765`
- 1h: commodity avg `-0.065` n `12`; crypto_alt avg `0.1381` n `228`; crypto_major avg `0.1649` n `8`; equity avg `0.2643` n `88`; fx avg `-0.0287` n `6`; index avg `0.0771` n `23`; metal avg `0.1292` n `20`; unknown avg `-0.2687` n `765`
- 4h: commodity avg `-0.0584` n `12`; crypto_alt avg `0.1102` n `228`; crypto_major avg `-0.1513` n `8`; equity avg `1.0261` n `88`; fx avg `-0.0892` n `6`; index avg `0.3296` n `23`; metal avg `0.4897` n `20`; unknown avg `9.9097` n `763`
- 24h: commodity avg `-0.2444` n `12`; crypto_alt avg `0.5704` n `228`; crypto_major avg `1.7391` n `8`; equity avg `2.773` n `88`; fx avg `0.0975` n `6`; index avg `0.4891` n `23`; metal avg `-0.4319` n `20`; unknown avg `12.2406` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
