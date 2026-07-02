# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T00:37:30.623684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.1433` n `228`; crypto_major avg `-0.2378` n `8`; equity avg `0.0184` n `88`; fx avg `0.0151` n `6`; index avg `0.0102` n `25`; metal avg `-0.0241` n `20`; unknown avg `-0.0268` n `763`
- 1h: commodity avg `-0.0442` n `12`; crypto_alt avg `-0.2927` n `228`; crypto_major avg `-0.5716` n `8`; equity avg `-0.2158` n `88`; fx avg `0.0192` n `6`; index avg `-0.1028` n `25`; metal avg `0.0206` n `20`; unknown avg `1.1842` n `763`
- 4h: commodity avg `-0.052` n `12`; crypto_alt avg `-0.1267` n `228`; crypto_major avg `-0.4416` n `8`; equity avg `-0.1885` n `88`; fx avg `0.0575` n `6`; index avg `-0.0852` n `25`; metal avg `0.0762` n `20`; unknown avg `84.1205` n `763`
- 24h: commodity avg `-0.6531` n `12`; crypto_alt avg `1.3685` n `228`; crypto_major avg `0.7671` n `8`; equity avg `-1.9362` n `88`; fx avg `0.0206` n `6`; index avg `-0.6163` n `25`; metal avg `0.3746` n `20`; unknown avg `86.7777` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
