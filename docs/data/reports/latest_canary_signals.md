# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T00:07:26.806221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0628` n `13`; crypto_alt avg `-0.0832` n `238`; crypto_major avg `0.0019` n `8`; equity avg `0.0817` n `156`; fx avg `0.0038` n `6`; index avg `0.0078` n `27`; metal avg `-0.0042` n `20`; unknown avg `-0.1911` n `1250`
- 1h: commodity avg `-0.0352` n `13`; crypto_alt avg `0.2652` n `238`; crypto_major avg `0.3301` n `8`; equity avg `0.1632` n `156`; fx avg `0.0195` n `6`; index avg `0.0149` n `27`; metal avg `-0.0024` n `20`; unknown avg `0.3067` n `1249`
- 4h: commodity avg `-0.1153` n `13`; crypto_alt avg `1.1987` n `238`; crypto_major avg `0.4652` n `8`; equity avg `0.3411` n `156`; fx avg `-0.0092` n `6`; index avg `0.0173` n `27`; metal avg `-0.0344` n `20`; unknown avg `0.3961` n `1175`
- 24h: commodity avg `0.0168` n `13`; crypto_alt avg `2.7409` n `238`; crypto_major avg `0.4008` n `8`; equity avg `-2.5859` n `156`; fx avg `-0.1278` n `6`; index avg `-0.2185` n `27`; metal avg `-0.8495` n `20`; unknown avg `4.1023` n `1020`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
