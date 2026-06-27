# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T05:22:25.978949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.91` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.0595` n `228`; crypto_major avg `0.1194` n `8`; equity avg `0.0057` n `88`; fx avg `0.0043` n `6`; index avg `-0.0029` n `23`; metal avg `0.0009` n `20`; unknown avg `2.098` n `764`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.4991` n `228`; crypto_major avg `-0.376` n `8`; equity avg `-0.0498` n `88`; fx avg `0.0069` n `6`; index avg `-0.0183` n `23`; metal avg `-0.0219` n `20`; unknown avg `11.6636` n `764`
- 4h: commodity avg `-0.027` n `12`; crypto_alt avg `-0.0627` n `228`; crypto_major avg `0.2667` n `8`; equity avg `0.1521` n `88`; fx avg `0.0082` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0003` n `20`; unknown avg `-0.9317` n `764`
- 24h: commodity avg `-0.065` n `12`; crypto_alt avg `2.2297` n `228`; crypto_major avg `2.0875` n `8`; equity avg `1.8476` n `87`; fx avg `-0.0091` n `6`; index avg `0.1252` n `23`; metal avg `1.2098` n `20`; unknown avg `-0.4582` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
