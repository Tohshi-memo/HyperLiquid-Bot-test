# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T19:07:32.128454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `13`; crypto_alt avg `0.3789` n `238`; crypto_major avg `0.4475` n `8`; equity avg `0.515` n `156`; fx avg `0.0065` n `6`; index avg `0.0684` n `27`; metal avg `0.0345` n `20`; unknown avg `5.6682` n `1255`
- 1h: commodity avg `0.0101` n `13`; crypto_alt avg `-0.4917` n `238`; crypto_major avg `-0.4834` n `8`; equity avg `-0.0355` n `156`; fx avg `0.0127` n `6`; index avg `-0.0218` n `27`; metal avg `-0.039` n `20`; unknown avg `0.0179` n `1255`
- 4h: commodity avg `0.0885` n `13`; crypto_alt avg `-0.9605` n `238`; crypto_major avg `-1.1613` n `8`; equity avg `-1.6677` n `156`; fx avg `0.0544` n `6`; index avg `-0.1805` n `27`; metal avg `-0.2391` n `20`; unknown avg `2.1546` n `1249`
- 24h: commodity avg `0.4528` n `13`; crypto_alt avg `-4.6003` n `238`; crypto_major avg `-4.3948` n `8`; equity avg `-5.9795` n `156`; fx avg `-0.0718` n `6`; index avg `-0.5507` n `27`; metal avg `-1.0407` n `20`; unknown avg `240.1947` n `1038`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
