# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T02:37:17.640637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0356` n `12`; crypto_alt avg `0.1396` n `228`; crypto_major avg `0.0039` n `8`; equity avg `0.1325` n `69`; fx avg `0.0016` n `6`; index avg `-0.4887` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.3434` n `422`
- 1h: commodity avg `-0.0566` n `12`; crypto_alt avg `0.1173` n `228`; crypto_major avg `-0.0916` n `8`; equity avg `0.2572` n `69`; fx avg `0.0145` n `6`; index avg `-0.6898` n `23`; metal avg `0.2653` n `18`; unknown avg `0.101` n `421`
- 4h: commodity avg `0.1912` n `12`; crypto_alt avg `0.2105` n `228`; crypto_major avg `-0.441` n `8`; equity avg `0.1403` n `69`; fx avg `0.088` n `6`; index avg `-0.7069` n `23`; metal avg `0.5572` n `18`; unknown avg `-0.0446` n `421`
- 24h: commodity avg `1.0383` n `12`; crypto_alt avg `0.8236` n `228`; crypto_major avg `-0.2863` n `8`; equity avg `0.6691` n `69`; fx avg `0.0592` n `6`; index avg `-0.3207` n `23`; metal avg `0.4692` n `18`; unknown avg `1.4416` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2834`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2509`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
