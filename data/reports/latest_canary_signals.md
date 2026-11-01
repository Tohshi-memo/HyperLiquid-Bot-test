# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T03:08:01.788389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `0.1658` n `238`; crypto_major avg `0.0868` n `8`; equity avg `0.0371` n `156`; fx avg `0.0031` n `6`; index avg `0.0228` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.2497` n `1256`
- 1h: commodity avg `-0.0458` n `13`; crypto_alt avg `-0.1667` n `238`; crypto_major avg `-0.1467` n `8`; equity avg `-0.0174` n `156`; fx avg `0.0069` n `6`; index avg `0.0175` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.6584` n `1254`
- 4h: commodity avg `0.0238` n `13`; crypto_alt avg `-0.0544` n `238`; crypto_major avg `0.1416` n `8`; equity avg `0.0743` n `156`; fx avg `0.0109` n `6`; index avg `0.0003` n `27`; metal avg `0.0013` n `20`; unknown avg `1.145` n `1202`
- 24h: commodity avg `-0.0447` n `13`; crypto_alt avg `-0.5323` n `238`; crypto_major avg `-0.2894` n `8`; equity avg `0.0325` n `156`; fx avg `0.0145` n `6`; index avg `-0.0513` n `27`; metal avg `0.0565` n `20`; unknown avg `1.7897` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
