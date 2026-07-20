# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T15:37:34.872895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.0471` n `8`; equity avg `0.0479` n `98`; fx avg `0.0026` n `6`; index avg `0.0371` n `25`; metal avg `0.0096` n `20`; unknown avg `0.0129` n `770`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `0.4487` n `230`; crypto_major avg `0.7289` n `8`; equity avg `0.2427` n `98`; fx avg `-0.0512` n `6`; index avg `0.0093` n `25`; metal avg `0.0231` n `20`; unknown avg `-0.0634` n `770`
- 4h: commodity avg `0.3176` n `12`; crypto_alt avg `0.073` n `230`; crypto_major avg `-0.0869` n `8`; equity avg `-0.6404` n `98`; fx avg `-0.0858` n `6`; index avg `-0.0962` n `25`; metal avg `-0.1247` n `20`; unknown avg `-0.0799` n `770`
- 24h: commodity avg `-0.6084` n `12`; crypto_alt avg `0.792` n `230`; crypto_major avg `0.3997` n `8`; equity avg `0.4936` n `97`; fx avg `-0.1427` n `6`; index avg `0.1707` n `25`; metal avg `0.2079` n `20`; unknown avg `-0.0225` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
