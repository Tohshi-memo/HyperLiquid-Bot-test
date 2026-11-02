# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T03:22:26.726084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `13`; crypto_alt avg `0.0482` n `238`; crypto_major avg `-0.0251` n `8`; equity avg `0.2654` n `156`; fx avg `0.0181` n `6`; index avg `0.0346` n `27`; metal avg `-0.0035` n `20`; unknown avg `0.1562` n `1263`
- 1h: commodity avg `-0.1234` n `13`; crypto_alt avg `0.0607` n `238`; crypto_major avg `0.0132` n `8`; equity avg `0.3626` n `156`; fx avg `0.0556` n `6`; index avg `0.0323` n `27`; metal avg `-0.0919` n `20`; unknown avg `-0.2995` n `1257`
- 4h: commodity avg `-0.3092` n `13`; crypto_alt avg `0.1119` n `238`; crypto_major avg `0.5858` n `8`; equity avg `1.0505` n `156`; fx avg `0.1934` n `6`; index avg `0.2547` n `27`; metal avg `-0.0571` n `20`; unknown avg `1.8644` n `1241`
- 24h: commodity avg `-0.3484` n `13`; crypto_alt avg `-0.3731` n `238`; crypto_major avg `0.4646` n `8`; equity avg `1.3298` n `156`; fx avg `0.2037` n `6`; index avg `0.3058` n `27`; metal avg `0.049` n `20`; unknown avg `3.0236` n `1122`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
