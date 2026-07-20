# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T03:52:29.006182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0358` n `230`; crypto_major avg `0.0925` n `8`; equity avg `0.197` n `98`; fx avg `-0.0005` n `6`; index avg `0.0554` n `25`; metal avg `0.006` n `20`; unknown avg `-0.05` n `769`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `-0.1619` n `230`; crypto_major avg `-0.0938` n `8`; equity avg `0.0578` n `98`; fx avg `-0.0018` n `6`; index avg `-0.0065` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.1595` n `769`
- 4h: commodity avg `-0.0339` n `12`; crypto_alt avg `0.2092` n `230`; crypto_major avg `0.1532` n `8`; equity avg `0.1252` n `98`; fx avg `-0.0486` n `6`; index avg `0.0946` n `25`; metal avg `0.305` n `20`; unknown avg `-0.1219` n `769`
- 24h: commodity avg `-0.071` n `12`; crypto_alt avg `0.1933` n `230`; crypto_major avg `0.3507` n `8`; equity avg `0.4554` n `97`; fx avg `-0.0128` n `6`; index avg `0.0762` n `25`; metal avg `0.1393` n `20`; unknown avg `0.0404` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0896`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
