# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T19:07:33.395918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `-0.0519` n `235`; crypto_major avg `-0.0229` n `8`; equity avg `-0.0711` n `150`; fx avg `0.009` n `6`; index avg `-0.0073` n `26`; metal avg `0.0115` n `20`; unknown avg `-0.2349` n `1090`
- 1h: commodity avg `-0.2121` n `13`; crypto_alt avg `-0.425` n `235`; crypto_major avg `-0.2799` n `8`; equity avg `-0.0554` n `150`; fx avg `0.009` n `6`; index avg `0.0199` n `26`; metal avg `0.0356` n `20`; unknown avg `3.2262` n `1090`
- 4h: commodity avg `-0.4188` n `13`; crypto_alt avg `0.367` n `235`; crypto_major avg `-0.1009` n `8`; equity avg `0.2744` n `150`; fx avg `0.0169` n `6`; index avg `0.0662` n `26`; metal avg `0.0904` n `20`; unknown avg `1.7385` n `1020`
- 24h: commodity avg `-0.2756` n `13`; crypto_alt avg `2.5697` n `235`; crypto_major avg `1.2878` n `8`; equity avg `1.4084` n `150`; fx avg `0.0379` n `6`; index avg `0.2299` n `26`; metal avg `0.6833` n `20`; unknown avg `2.4685` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1409`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1321`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1124`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `669`, weak_sample_signal
