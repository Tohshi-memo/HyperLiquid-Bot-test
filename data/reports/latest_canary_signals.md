# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T11:52:28.421028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1129` n `12`; crypto_alt avg `-0.3203` n `233`; crypto_major avg `-0.1892` n `8`; equity avg `-0.2171` n `134`; fx avg `-0.0167` n `6`; index avg `-0.0507` n `26`; metal avg `-0.0876` n `20`; unknown avg `0.1029` n `797`
- 1h: commodity avg `0.1243` n `12`; crypto_alt avg `0.0978` n `233`; crypto_major avg `0.008` n `8`; equity avg `-0.276` n `134`; fx avg `-0.0084` n `6`; index avg `-0.0716` n `26`; metal avg `-0.1107` n `20`; unknown avg `-0.0923` n `795`
- 4h: commodity avg `0.211` n `12`; crypto_alt avg `-0.1821` n `233`; crypto_major avg `-0.2615` n `8`; equity avg `-0.5813` n `134`; fx avg `0.0349` n `6`; index avg `-0.1239` n `26`; metal avg `-0.6278` n `20`; unknown avg `-0.0589` n `789`
- 24h: commodity avg `0.1332` n `12`; crypto_alt avg `-4.4673` n `233`; crypto_major avg `-3.0959` n `8`; equity avg `-1.2365` n `134`; fx avg `0.0978` n `6`; index avg `-0.1159` n `26`; metal avg `-0.4697` n `20`; unknown avg `-0.7575` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
