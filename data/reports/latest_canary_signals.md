# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T22:22:28.965872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `13`; crypto_alt avg `-0.105` n `234`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0201` n `142`; fx avg `-0.0035` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0158` n `20`; unknown avg `0.2364` n `985`
- 1h: commodity avg `-0.057` n `13`; crypto_alt avg `-0.142` n `234`; crypto_major avg `0.0335` n `8`; equity avg `0.0159` n `142`; fx avg `-0.0055` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0454` n `20`; unknown avg `-0.1458` n `943`
- 4h: commodity avg `0.074` n `13`; crypto_alt avg `-0.493` n `234`; crypto_major avg `-0.2759` n `8`; equity avg `0.175` n `142`; fx avg `0.0302` n `6`; index avg `0.0516` n `26`; metal avg `0.0372` n `20`; unknown avg `-0.1217` n `891`
- 24h: commodity avg `0.1306` n `13`; crypto_alt avg `-0.3706` n `234`; crypto_major avg `-0.2887` n `8`; equity avg `0.9872` n `142`; fx avg `-0.1017` n `6`; index avg `0.1766` n `26`; metal avg `-0.0451` n `20`; unknown avg `0.0494` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
