# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T23:18:09.664558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.0652` n `238`; crypto_major avg `-0.0757` n `8`; equity avg `0.0622` n `156`; fx avg `0.0017` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0092` n `20`; unknown avg `0.4124` n `1259`
- 1h: commodity avg `0.0004` n `13`; crypto_alt avg `0.4056` n `238`; crypto_major avg `0.2337` n `8`; equity avg `0.1282` n `156`; fx avg `-0.006` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0024` n `20`; unknown avg `0.162` n `1255`
- 4h: commodity avg `-0.2559` n `13`; crypto_alt avg `1.662` n `238`; crypto_major avg `0.5523` n `8`; equity avg `0.9237` n `156`; fx avg `-0.0483` n `6`; index avg `0.1056` n `27`; metal avg `0.0958` n `20`; unknown avg `1.2668` n `1149`
- 24h: commodity avg `0.0655` n `13`; crypto_alt avg `1.5082` n `238`; crypto_major avg `-0.8464` n `8`; equity avg `-2.5965` n `156`; fx avg `-0.1524` n `6`; index avg `-0.2474` n `27`; metal avg `-0.9116` n `20`; unknown avg `1.0822` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
