# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T19:52:39.872724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0651` n `13`; crypto_alt avg `-0.0083` n `239`; crypto_major avg `0.0254` n `8`; equity avg `-0.0307` n `158`; fx avg `-0.0005` n `6`; index avg `-0.0202` n `27`; metal avg `-0.0023` n `20`; unknown avg `-0.0666` n `1263`
- 1h: commodity avg `0.1241` n `13`; crypto_alt avg `-0.0838` n `239`; crypto_major avg `-0.1442` n `8`; equity avg `-0.2276` n `158`; fx avg `0.0069` n `6`; index avg `-0.048` n `27`; metal avg `-0.0448` n `20`; unknown avg `160.3086` n `1257`
- 4h: commodity avg `0.2987` n `13`; crypto_alt avg `-0.3393` n `239`; crypto_major avg `-0.4932` n `8`; equity avg `-0.4751` n `158`; fx avg `0.0357` n `6`; index avg `-0.0855` n `27`; metal avg `-0.1785` n `20`; unknown avg `-0.4514` n `1215`
- 24h: commodity avg `0.2571` n `13`; crypto_alt avg `1.4249` n `239`; crypto_major avg `1.4772` n `8`; equity avg `1.3202` n `158`; fx avg `0.0828` n `6`; index avg `0.0922` n `27`; metal avg `-0.5027` n `20`; unknown avg `371.3021` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
