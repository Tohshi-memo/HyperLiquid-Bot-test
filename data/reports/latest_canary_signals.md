# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T18:22:20.193031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.1348` n `228`; crypto_major avg `-0.1185` n `8`; equity avg `0.0216` n `69`; fx avg `0.0014` n `6`; index avg `-0.0112` n `23`; metal avg `0.0` n `18`; unknown avg `-0.1486` n `421`
- 1h: commodity avg `0.0852` n `12`; crypto_alt avg `0.2034` n `228`; crypto_major avg `0.0463` n `8`; equity avg `0.1088` n `69`; fx avg `0.0015` n `6`; index avg `0.0588` n `23`; metal avg `-0.0235` n `18`; unknown avg `-0.1497` n `421`
- 4h: commodity avg `0.1858` n `12`; crypto_alt avg `-0.0539` n `228`; crypto_major avg `-0.3425` n `8`; equity avg `0.1578` n `69`; fx avg `-0.0039` n `6`; index avg `0.2992` n `23`; metal avg `-0.0562` n `18`; unknown avg `-0.021` n `421`
- 24h: commodity avg `0.8` n `12`; crypto_alt avg `-1.3832` n `228`; crypto_major avg `-0.754` n `8`; equity avg `0.9401` n `69`; fx avg `-0.0088` n `6`; index avg `0.1427` n `23`; metal avg `-0.1531` n `18`; unknown avg `0.1556` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
