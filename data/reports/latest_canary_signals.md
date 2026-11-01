# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T17:07:29.171741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0551` n `238`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0032` n `156`; fx avg `-0.0149` n `6`; index avg `-0.0003` n `27`; metal avg `0.0054` n `20`; unknown avg `159.7769` n `1257`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.0621` n `238`; crypto_major avg `-0.0302` n `8`; equity avg `0.039` n `156`; fx avg `0.006` n `6`; index avg `0.0217` n `27`; metal avg `0.0145` n `20`; unknown avg `159.5877` n `1257`
- 4h: commodity avg `-0.0519` n `13`; crypto_alt avg `-0.4661` n `238`; crypto_major avg `-0.069` n `8`; equity avg `0.0189` n `156`; fx avg `0.0134` n `6`; index avg `0.0534` n `27`; metal avg `-0.0014` n `20`; unknown avg `0.3772` n `1245`
- 24h: commodity avg `0.0143` n `13`; crypto_alt avg `-0.6054` n `238`; crypto_major avg `0.2177` n `8`; equity avg `0.5007` n `156`; fx avg `-0.0005` n `6`; index avg `0.098` n `27`; metal avg `0.0515` n `20`; unknown avg `4.7759` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
