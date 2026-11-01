# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T08:37:26.523439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `0.1536` n `238`; crypto_major avg `0.233` n `8`; equity avg `0.0908` n `156`; fx avg `0.0021` n `6`; index avg `0.0037` n `27`; metal avg `0.0066` n `20`; unknown avg `-0.0468` n `1263`
- 1h: commodity avg `0.0023` n `13`; crypto_alt avg `0.0184` n `238`; crypto_major avg `0.1876` n `8`; equity avg `0.0898` n `156`; fx avg `-0.0019` n `6`; index avg `0.0042` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.0984` n `1241`
- 4h: commodity avg `-0.023` n `13`; crypto_alt avg `0.289` n `238`; crypto_major avg `0.2274` n `8`; equity avg `0.2008` n `156`; fx avg `0.0085` n `6`; index avg `0.021` n `27`; metal avg `0.0167` n `20`; unknown avg `0.9999` n `1222`
- 24h: commodity avg `-0.0066` n `13`; crypto_alt avg `1.0336` n `238`; crypto_major avg `0.9721` n `8`; equity avg `0.4846` n `156`; fx avg `-0.0146` n `6`; index avg `0.0154` n `27`; metal avg `0.0935` n `20`; unknown avg `2.6644` n `996`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
