# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T19:42:09.889505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0868` n `13`; crypto_alt avg `0.3306` n `238`; crypto_major avg `0.2196` n `8`; equity avg `0.1491` n `156`; fx avg `0.0054` n `6`; index avg `0.0322` n `27`; metal avg `0.0207` n `20`; unknown avg `7.2248` n `1259`
- 1h: commodity avg `-0.1203` n `13`; crypto_alt avg `0.4781` n `238`; crypto_major avg `0.3382` n `8`; equity avg `0.8737` n `156`; fx avg `0.015` n `6`; index avg `0.0895` n `27`; metal avg `0.0365` n `20`; unknown avg `13.3535` n `1253`
- 4h: commodity avg `-0.048` n `13`; crypto_alt avg `-0.2512` n `238`; crypto_major avg `-0.5406` n `8`; equity avg `-0.7843` n `156`; fx avg `0.0427` n `6`; index avg `-0.0957` n `27`; metal avg `-0.1458` n `20`; unknown avg `7.3618` n `1249`
- 24h: commodity avg `0.2548` n `13`; crypto_alt avg `-4.449` n `238`; crypto_major avg `-4.1832` n `8`; equity avg `-5.7889` n `156`; fx avg `-0.0821` n `6`; index avg `-0.5389` n `27`; metal avg `-1.0437` n `20`; unknown avg `234.462` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
