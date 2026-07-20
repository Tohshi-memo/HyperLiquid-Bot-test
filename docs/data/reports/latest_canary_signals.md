# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T03:37:29.847806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `-0.0064` n `230`; crypto_major avg `0.0059` n `8`; equity avg `0.0022` n `98`; fx avg `-0.0001` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0351` n `20`; unknown avg `-0.1185` n `769`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `0.0576` n `8`; equity avg `0.1464` n `98`; fx avg `0.0111` n `6`; index avg `-0.0322` n `25`; metal avg `0.0948` n `20`; unknown avg `-0.1215` n `769`
- 4h: commodity avg `-0.0403` n `12`; crypto_alt avg `0.2013` n `230`; crypto_major avg `0.0751` n `8`; equity avg `-0.1128` n `98`; fx avg `-0.0491` n `6`; index avg `-0.022` n `25`; metal avg `0.3145` n `20`; unknown avg `-0.3165` n `767`
- 24h: commodity avg `-0.0717` n `12`; crypto_alt avg `0.0985` n `230`; crypto_major avg `0.2595` n `8`; equity avg `0.2489` n `97`; fx avg `-0.0159` n `6`; index avg `0.0091` n `25`; metal avg `0.1317` n `20`; unknown avg `-0.0185` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0755`, n `666`, weak_sample_signal
