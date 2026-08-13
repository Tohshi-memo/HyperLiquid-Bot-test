# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T18:52:27.534109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.1244` n `230`; crypto_major avg `0.2303` n `8`; equity avg `0.0853` n `113`; fx avg `-0.0044` n `6`; index avg `0.0156` n `25`; metal avg `-0.0377` n `20`; unknown avg `0.1862` n `787`
- 1h: commodity avg `-0.1193` n `12`; crypto_alt avg `-0.0166` n `230`; crypto_major avg `0.1351` n `8`; equity avg `0.0215` n `113`; fx avg `0.0008` n `6`; index avg `0.0065` n `25`; metal avg `-0.052` n `20`; unknown avg `0.078` n `787`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.9406` n `230`; crypto_major avg `-0.4423` n `8`; equity avg `-0.0215` n `113`; fx avg `-0.0045` n `6`; index avg `0.0294` n `25`; metal avg `-0.1469` n `20`; unknown avg `0.1657` n `787`
- 24h: commodity avg `-0.5537` n `12`; crypto_alt avg `-0.6171` n `230`; crypto_major avg `0.0552` n `8`; equity avg `1.3721` n `113`; fx avg `0.003` n `6`; index avg `0.3236` n `25`; metal avg `-0.5149` n `20`; unknown avg `0.0481` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2338`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
