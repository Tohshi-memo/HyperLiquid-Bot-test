# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T16:07:25.946056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `13`; crypto_alt avg `-0.0613` n `238`; crypto_major avg `0.021` n `8`; equity avg `0.0016` n `156`; fx avg `-0.0127` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0107` n `20`; unknown avg `-0.0201` n `1243`
- 1h: commodity avg `-0.0943` n `13`; crypto_alt avg `-0.3698` n `238`; crypto_major avg `-0.1766` n `8`; equity avg `-0.0095` n `156`; fx avg `-0.0077` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0039` n `20`; unknown avg `-0.168` n `1243`
- 4h: commodity avg `-0.0649` n `13`; crypto_alt avg `-0.2137` n `238`; crypto_major avg `-0.1831` n `8`; equity avg `-0.0591` n `156`; fx avg `0.0142` n `6`; index avg `0.029` n `27`; metal avg `-0.0122` n `20`; unknown avg `-0.0641` n `1245`
- 24h: commodity avg `-0.0271` n `13`; crypto_alt avg `-0.7515` n `238`; crypto_major avg `0.129` n `8`; equity avg `0.4447` n `156`; fx avg `-0.0017` n `6`; index avg `0.0836` n `27`; metal avg `0.045` n `20`; unknown avg `1.5612` n `1010`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
