# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T21:13:44.640154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `0.1104` n `228`; crypto_major avg `0.1628` n `8`; equity avg `0.0536` n `69`; fx avg `-0.0124` n `6`; index avg `-0.2321` n `23`; metal avg `-0.0147` n `18`; unknown avg `-0.051` n `421`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `0.2904` n `228`; crypto_major avg `0.3028` n `8`; equity avg `0.0679` n `69`; fx avg `-0.0196` n `6`; index avg `0.0418` n `23`; metal avg `-0.0228` n `18`; unknown avg `1.2534` n `421`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `1.1945` n `228`; crypto_major avg `0.6272` n `8`; equity avg `0.1821` n `69`; fx avg `-0.0245` n `6`; index avg `0.1163` n `23`; metal avg `-0.071` n `18`; unknown avg `0.6522` n `421`
- 24h: commodity avg `0.4323` n `12`; crypto_alt avg `-0.755` n `228`; crypto_major avg `-0.2532` n `8`; equity avg `0.7672` n `69`; fx avg `-0.0411` n `6`; index avg `0.2007` n `23`; metal avg `-0.1797` n `18`; unknown avg `1.7049` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2827`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
