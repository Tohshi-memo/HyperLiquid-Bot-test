# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T07:37:30.032084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.135` n `12`; crypto_alt avg `0.1363` n `230`; crypto_major avg `0.1349` n `8`; equity avg `0.2458` n `98`; fx avg `0.0011` n `6`; index avg `0.0483` n `25`; metal avg `0.1761` n `20`; unknown avg `0.379` n `769`
- 1h: commodity avg `-0.2715` n `12`; crypto_alt avg `0.6757` n `230`; crypto_major avg `0.5113` n `8`; equity avg `0.4023` n `98`; fx avg `0.0501` n `6`; index avg `0.0742` n `25`; metal avg `0.1995` n `20`; unknown avg `-0.091` n `769`
- 4h: commodity avg `-0.1907` n `12`; crypto_alt avg `-0.3858` n `230`; crypto_major avg `-0.7032` n `8`; equity avg `0.0133` n `98`; fx avg `0.0097` n `6`; index avg `0.0185` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.3727` n `753`
- 24h: commodity avg `-0.2684` n `12`; crypto_alt avg `-0.2819` n `230`; crypto_major avg `-0.5927` n `8`; equity avg `0.1243` n `97`; fx avg `-0.0191` n `6`; index avg `0.0379` n `25`; metal avg `0.1616` n `20`; unknown avg `-0.1424` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0964`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0883`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
