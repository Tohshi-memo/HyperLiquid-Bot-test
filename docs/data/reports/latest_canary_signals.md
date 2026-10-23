# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T12:07:28.909777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1115` n `13`; crypto_alt avg `-0.1827` n `237`; crypto_major avg `-0.228` n `8`; equity avg `-0.2276` n `152`; fx avg `-0.009` n `6`; index avg `-0.0496` n `26`; metal avg `-0.0211` n `20`; unknown avg `0.0695` n `1225`
- 1h: commodity avg `-0.0088` n `13`; crypto_alt avg `0.2235` n `237`; crypto_major avg `0.136` n `8`; equity avg `-0.1841` n `152`; fx avg `-0.0355` n `6`; index avg `-0.0423` n `26`; metal avg `-0.0284` n `20`; unknown avg `0.6345` n `1225`
- 4h: commodity avg `0.0621` n `13`; crypto_alt avg `-0.0978` n `237`; crypto_major avg `-0.1781` n `8`; equity avg `-0.7781` n `152`; fx avg `-0.0628` n `6`; index avg `-0.1176` n `26`; metal avg `0.0674` n `20`; unknown avg `1.2735` n `1195`
- 24h: commodity avg `0.3115` n `13`; crypto_alt avg `0.1144` n `237`; crypto_major avg `0.2743` n `8`; equity avg `-1.7674` n `152`; fx avg `-0.0656` n `6`; index avg `-0.2345` n `26`; metal avg `-0.3338` n `20`; unknown avg `49.6715` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
