# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T00:22:28.883638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.0565` n `230`; crypto_major avg `0.1028` n `8`; equity avg `-0.1722` n `108`; fx avg `-0.0092` n `6`; index avg `-0.0595` n `25`; metal avg `0.0331` n `20`; unknown avg `-0.0872` n `782`
- 1h: commodity avg `-0.0609` n `12`; crypto_alt avg `0.1374` n `230`; crypto_major avg `0.1307` n `8`; equity avg `-0.2393` n `108`; fx avg `0.0035` n `6`; index avg `-0.0734` n `25`; metal avg `0.115` n `20`; unknown avg `0.1824` n `782`
- 4h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.0058` n `230`; crypto_major avg `-0.2997` n `8`; equity avg `-0.2587` n `108`; fx avg `0.0066` n `6`; index avg `-0.0652` n `25`; metal avg `0.1812` n `20`; unknown avg `0.2056` n `782`
- 24h: commodity avg `-0.149` n `12`; crypto_alt avg `0.8499` n `230`; crypto_major avg `1.038` n `8`; equity avg `-1.3446` n `108`; fx avg `-0.0092` n `6`; index avg `-0.2614` n `25`; metal avg `0.973` n `20`; unknown avg `1.2705` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
