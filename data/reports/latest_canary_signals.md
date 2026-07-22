# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T07:22:31.971560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.0643` n `230`; crypto_major avg `0.0731` n `8`; equity avg `0.1438` n `98`; fx avg `0.0131` n `6`; index avg `0.0291` n `25`; metal avg `0.0873` n `20`; unknown avg `-0.0106` n `772`
- 1h: commodity avg `0.0942` n `12`; crypto_alt avg `0.02` n `230`; crypto_major avg `0.102` n `8`; equity avg `0.1406` n `98`; fx avg `-0.0049` n `6`; index avg `0.0239` n `25`; metal avg `-0.0391` n `20`; unknown avg `-0.0017` n `772`
- 4h: commodity avg `0.199` n `12`; crypto_alt avg `-0.7961` n `230`; crypto_major avg `-0.9375` n `8`; equity avg `-0.981` n `98`; fx avg `-0.0268` n `6`; index avg `-0.2199` n `25`; metal avg `-0.1865` n `20`; unknown avg `-0.2455` n `739`
- 24h: commodity avg `0.6337` n `12`; crypto_alt avg `-1.0953` n `230`; crypto_major avg `-1.4428` n `8`; equity avg `0.8538` n `98`; fx avg `0.0132` n `6`; index avg `0.0397` n `25`; metal avg `0.3413` n `20`; unknown avg `-0.003` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0823`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.07`, n `666`, weak_sample_signal
