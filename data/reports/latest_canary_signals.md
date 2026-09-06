# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T22:37:25.538316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.332` n `232`; crypto_major avg `0.4408` n `8`; equity avg `-0.0035` n `134`; fx avg `-0.0113` n `6`; index avg `0.0067` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.3083` n `793`
- 1h: commodity avg `0.0197` n `12`; crypto_alt avg `-0.3012` n `232`; crypto_major avg `-0.2542` n `8`; equity avg `-0.0586` n `134`; fx avg `0.0099` n `6`; index avg `0.0014` n `26`; metal avg `-0.0418` n `20`; unknown avg `0.3204` n `791`
- 4h: commodity avg `0.0084` n `12`; crypto_alt avg `0.2613` n `232`; crypto_major avg `0.0855` n `8`; equity avg `-0.0065` n `134`; fx avg `0.0356` n `6`; index avg `0.0119` n `26`; metal avg `-0.046` n `20`; unknown avg `0.8777` n `761`
- 24h: commodity avg `-0.0062` n `12`; crypto_alt avg `1.0494` n `232`; crypto_major avg `0.4878` n `8`; equity avg `0.2537` n `134`; fx avg `0.0282` n `6`; index avg `0.0037` n `26`; metal avg `-0.0872` n `20`; unknown avg `151.5206` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
