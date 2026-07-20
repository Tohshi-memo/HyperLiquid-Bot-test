# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T02:52:28.653794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `0.1642` n `230`; crypto_major avg `0.2441` n `8`; equity avg `0.2867` n `98`; fx avg `0.0125` n `6`; index avg `0.0294` n `25`; metal avg `0.0765` n `20`; unknown avg `-0.0595` n `769`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.0565` n `230`; crypto_major avg `-0.0269` n `8`; equity avg `0.1309` n `98`; fx avg `-0.0005` n `6`; index avg `0.0268` n `25`; metal avg `0.1794` n `20`; unknown avg `-0.0132` n `769`
- 4h: commodity avg `-0.122` n `12`; crypto_alt avg `0.1701` n `230`; crypto_major avg `0.2835` n `8`; equity avg `-0.0362` n `98`; fx avg `-0.0425` n `6`; index avg `0.0724` n `25`; metal avg `0.2641` n `20`; unknown avg `2.6369` n `767`
- 24h: commodity avg `-0.0526` n `12`; crypto_alt avg `0.1505` n `230`; crypto_major avg `0.2216` n `8`; equity avg `0.3634` n `97`; fx avg `-0.0104` n `6`; index avg `0.0869` n `25`; metal avg `0.1354` n `20`; unknown avg `0.0745` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0819`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0762`, n `666`, weak_sample_signal
