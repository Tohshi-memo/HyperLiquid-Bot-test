# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T22:09:36.899590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0534` n `12`; crypto_alt avg `-0.1033` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `0.1082` n `114`; fx avg `0.0266` n `6`; index avg `0.0087` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.0214` n `792`
- 1h: commodity avg `0.0604` n `12`; crypto_alt avg `-0.0604` n `230`; crypto_major avg `-0.0287` n `8`; equity avg `0.1571` n `114`; fx avg `0.019` n `6`; index avg `0.0277` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0308` n `792`
- 4h: commodity avg `0.1743` n `12`; crypto_alt avg `-0.0782` n `230`; crypto_major avg `-0.0755` n `8`; equity avg `-0.1008` n `114`; fx avg `0.0092` n `6`; index avg `-0.0303` n `25`; metal avg `-0.04` n `20`; unknown avg `-0.0919` n `792`
- 24h: commodity avg `0.5339` n `12`; crypto_alt avg `0.811` n `230`; crypto_major avg `1.3666` n `8`; equity avg `1.2454` n `114`; fx avg `0.0584` n `6`; index avg `0.0693` n `25`; metal avg `0.2639` n `20`; unknown avg `0.2987` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
