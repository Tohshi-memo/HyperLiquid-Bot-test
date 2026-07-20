# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T19:52:29.733376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.1753` n `230`; crypto_major avg `0.2287` n `8`; equity avg `0.0091` n `98`; fx avg `0.007` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0137` n `20`; unknown avg `-0.1293` n `770`
- 1h: commodity avg `-0.1213` n `12`; crypto_alt avg `-0.124` n `230`; crypto_major avg `-0.1202` n `8`; equity avg `-0.319` n `98`; fx avg `0.0056` n `6`; index avg `-0.0251` n `25`; metal avg `-0.0284` n `20`; unknown avg `-0.2067` n `770`
- 4h: commodity avg `0.2132` n `12`; crypto_alt avg `0.0348` n `230`; crypto_major avg `-0.231` n `8`; equity avg `-0.5949` n `98`; fx avg `0.001` n `6`; index avg `-0.1444` n `25`; metal avg `-0.1225` n `20`; unknown avg `-0.2225` n `770`
- 24h: commodity avg `-0.3443` n `12`; crypto_alt avg `1.6756` n `230`; crypto_major avg `1.227` n `8`; equity avg `-0.0873` n `98`; fx avg `-0.1465` n `6`; index avg `0.0704` n `25`; metal avg `0.0881` n `20`; unknown avg `0.1475` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `666`, weak_sample_signal
