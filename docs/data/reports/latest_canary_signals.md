# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T01:56:49.613707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.4798` n `230`; crypto_major avg `-0.2917` n `8`; equity avg `0.0133` n `121`; fx avg `0.0016` n `6`; index avg `0.0069` n `25`; metal avg `0.0014` n `20`; unknown avg `3.2773` n `794`
- 1h: commodity avg `-0.0178` n `12`; crypto_alt avg `-1.126` n `230`; crypto_major avg `-0.7558` n `8`; equity avg `0.0046` n `121`; fx avg `-0.0071` n `6`; index avg `0.0103` n `25`; metal avg `0.0131` n `20`; unknown avg `3.8343` n `794`
- 4h: commodity avg `-0.0278` n `12`; crypto_alt avg `0.6549` n `230`; crypto_major avg `1.2539` n `8`; equity avg `0.2049` n `121`; fx avg `0.0352` n `6`; index avg `0.03` n `25`; metal avg `0.0119` n `20`; unknown avg `3.2203` n `794`
- 24h: commodity avg `0.0673` n `12`; crypto_alt avg `-3.068` n `230`; crypto_major avg `0.7226` n `8`; equity avg `-0.2` n `121`; fx avg `0.0961` n `6`; index avg `-0.04` n `25`; metal avg `-0.028` n `20`; unknown avg `2.8346` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
