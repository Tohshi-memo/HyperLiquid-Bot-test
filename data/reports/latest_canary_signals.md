# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T08:05:58.081745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `-0.0525` n `238`; crypto_major avg `0.0315` n `8`; equity avg `0.027` n `156`; fx avg `0.0006` n `6`; index avg `0.0024` n `27`; metal avg `0.0068` n `20`; unknown avg `-0.024` n `1241`
- 1h: commodity avg `0.0135` n `13`; crypto_alt avg `0.0238` n `238`; crypto_major avg `-0.0641` n `8`; equity avg `-0.0201` n `156`; fx avg `0.0108` n `6`; index avg `-0.0096` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.3197` n `1241`
- 4h: commodity avg `-0.0246` n `13`; crypto_alt avg `0.3448` n `238`; crypto_major avg `0.2548` n `8`; equity avg `0.1957` n `156`; fx avg `0.0013` n `6`; index avg `0.0278` n `27`; metal avg `0.0229` n `20`; unknown avg `0.7546` n `1222`
- 24h: commodity avg `0.0113` n `13`; crypto_alt avg `0.8872` n `238`; crypto_major avg `0.5352` n `8`; equity avg `0.3801` n `156`; fx avg `-0.0017` n `6`; index avg `0.0159` n `27`; metal avg `0.0884` n `20`; unknown avg `2.6907` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
