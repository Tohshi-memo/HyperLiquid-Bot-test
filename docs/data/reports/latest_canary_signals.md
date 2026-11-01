# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T06:52:27.859707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `13`; crypto_alt avg `0.0075` n `238`; crypto_major avg `0.1178` n `8`; equity avg `0.0037` n `156`; fx avg `-0.0105` n `6`; index avg `0.0089` n `27`; metal avg `0.0009` n `20`; unknown avg `0.3287` n `1263`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `-0.0152` n `238`; crypto_major avg `0.0655` n `8`; equity avg `0.0329` n `156`; fx avg `-0.0043` n `6`; index avg `0.0129` n `27`; metal avg `0.0296` n `20`; unknown avg `115.7306` n `1238`
- 4h: commodity avg `0.0016` n `13`; crypto_alt avg `0.6496` n `238`; crypto_major avg `0.3233` n `8`; equity avg `0.2779` n `156`; fx avg `-0.0124` n `6`; index avg `0.0486` n `27`; metal avg `0.026` n `20`; unknown avg `0.3572` n `1226`
- 24h: commodity avg `-0.0284` n `13`; crypto_alt avg `0.3159` n `238`; crypto_major avg `0.2548` n `8`; equity avg `0.2853` n `156`; fx avg `-0.0051` n `6`; index avg `0.0132` n `27`; metal avg `0.0535` n `20`; unknown avg `2.5262` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
