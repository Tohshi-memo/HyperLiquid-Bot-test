# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T14:37:29.517712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2504` n `12`; crypto_alt avg `-0.1363` n `228`; crypto_major avg `0.0036` n `8`; equity avg `0.0533` n `69`; fx avg `0.0068` n `6`; index avg `-0.0805` n `23`; metal avg `0.0441` n `18`; unknown avg `0.0711` n `422`
- 1h: commodity avg `0.6507` n `12`; crypto_alt avg `-0.6438` n `228`; crypto_major avg `-0.8617` n `8`; equity avg `0.193` n `69`; fx avg `-0.0239` n `6`; index avg `0.0391` n `23`; metal avg `-0.1056` n `18`; unknown avg `-0.1777` n `422`
- 4h: commodity avg `0.5283` n `12`; crypto_alt avg `-0.6486` n `228`; crypto_major avg `-1.3466` n `8`; equity avg `-0.7289` n `69`; fx avg `-0.0776` n `6`; index avg `-0.4462` n `23`; metal avg `-0.9951` n `18`; unknown avg `2.8296` n `416`
- 24h: commodity avg `1.4521` n `12`; crypto_alt avg `-0.5943` n `228`; crypto_major avg `-1.798` n `8`; equity avg `-0.7479` n `69`; fx avg `-0.0648` n `6`; index avg `0.0979` n `23`; metal avg `-0.6458` n `18`; unknown avg `4.3876` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2827`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
