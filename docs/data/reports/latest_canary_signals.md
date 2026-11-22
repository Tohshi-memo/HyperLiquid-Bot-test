# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T20:07:27.638214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `0.0144` n `239`; crypto_major avg `-0.0369` n `8`; equity avg `-0.0245` n `166`; fx avg `-0.0042` n `6`; index avg `-0.023` n `27`; metal avg `-0.0008` n `20`; unknown avg `2.3784` n `1246`
- 1h: commodity avg `-0.0251` n `13`; crypto_alt avg `-0.1132` n `239`; crypto_major avg `-0.1551` n `8`; equity avg `-0.0374` n `166`; fx avg `-0.0019` n `6`; index avg `-0.0431` n `27`; metal avg `-0.0012` n `20`; unknown avg `2.6861` n `1244`
- 4h: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.4016` n `239`; crypto_major avg `-0.2587` n `8`; equity avg `0.1245` n `166`; fx avg `0.0059` n `6`; index avg `-0.0151` n `27`; metal avg `-0.06` n `20`; unknown avg `0.2331` n `1233`
- 24h: commodity avg `-0.1347` n `13`; crypto_alt avg `0.5485` n `239`; crypto_major avg `0.3604` n `8`; equity avg `0.8949` n `166`; fx avg `-0.003` n `6`; index avg `0.0954` n `27`; metal avg `-0.0228` n `20`; unknown avg `262.137` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
