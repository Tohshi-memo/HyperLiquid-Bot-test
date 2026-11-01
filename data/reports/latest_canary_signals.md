# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T20:37:30.135496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `0.2579` n `238`; crypto_major avg `0.2787` n `8`; equity avg `0.0545` n `156`; fx avg `-0.0042` n `6`; index avg `0.003` n `27`; metal avg `0.0109` n `20`; unknown avg `21.3939` n `1263`
- 1h: commodity avg `-0.0254` n `13`; crypto_alt avg `0.2331` n `238`; crypto_major avg `0.1775` n `8`; equity avg `0.0156` n `156`; fx avg `-0.0218` n `6`; index avg `0.0051` n `27`; metal avg `0.0052` n `20`; unknown avg `165.2642` n `1235`
- 4h: commodity avg `0.0288` n `13`; crypto_alt avg `-0.627` n `238`; crypto_major avg `-0.3317` n `8`; equity avg `-0.2125` n `156`; fx avg `-0.0235` n `6`; index avg `-0.0478` n `27`; metal avg `-0.0103` n `20`; unknown avg `329.3461` n `1215`
- 24h: commodity avg `0.0452` n `13`; crypto_alt avg `-0.5196` n `238`; crypto_major avg `-0.1659` n `8`; equity avg `0.2494` n `156`; fx avg `-0.0109` n `6`; index avg `0.0488` n `27`; metal avg `0.0434` n `20`; unknown avg `4.0512` n `990`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
