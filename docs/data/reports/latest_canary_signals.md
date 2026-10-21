# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T04:22:31.684929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.1092` n `237`; crypto_major avg `-0.0425` n `8`; equity avg `0.0081` n `151`; fx avg `0.0011` n `6`; index avg `-0.0082` n `26`; metal avg `0.0449` n `20`; unknown avg `-0.0172` n `1200`
- 1h: commodity avg `-0.0321` n `13`; crypto_alt avg `-0.0058` n `237`; crypto_major avg `-0.163` n `8`; equity avg `-0.2474` n `151`; fx avg `-0.0454` n `6`; index avg `-0.0743` n `26`; metal avg `0.0171` n `20`; unknown avg `0.0904` n `1192`
- 4h: commodity avg `0.0979` n `13`; crypto_alt avg `-0.067` n `237`; crypto_major avg `-0.4064` n `8`; equity avg `-0.3224` n `151`; fx avg `-0.0092` n `6`; index avg `-0.0721` n `26`; metal avg `-0.1171` n `20`; unknown avg `2.8474` n `1191`
- 24h: commodity avg `0.0578` n `13`; crypto_alt avg `1.892` n `237`; crypto_major avg `1.1446` n `8`; equity avg `2.1462` n `151`; fx avg `-0.0017` n `6`; index avg `0.2821` n `26`; metal avg `-0.154` n `20`; unknown avg `212.2701` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
