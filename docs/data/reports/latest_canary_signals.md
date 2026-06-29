# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T15:07:29.126141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.2281` n `228`; crypto_major avg `-0.2943` n `8`; equity avg `0.1052` n `88`; fx avg `0.0087` n `6`; index avg `0.0333` n `23`; metal avg `-0.061` n `20`; unknown avg `-0.6204` n `764`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `-0.1543` n `228`; crypto_major avg `-0.1301` n `8`; equity avg `0.7333` n `88`; fx avg `0.0031` n `6`; index avg `0.0851` n `23`; metal avg `0.0572` n `20`; unknown avg `-0.0228` n `764`
- 4h: commodity avg `-0.0992` n `12`; crypto_alt avg `-0.62` n `228`; crypto_major avg `-0.4811` n `8`; equity avg `-0.7069` n `88`; fx avg `0.0571` n `6`; index avg `-0.1545` n `23`; metal avg `-0.1008` n `20`; unknown avg `0.1395` n `764`
- 24h: commodity avg `-0.6336` n `12`; crypto_alt avg `-0.9499` n `228`; crypto_major avg `-0.5706` n `8`; equity avg `-0.2295` n `88`; fx avg `0.128` n `6`; index avg `-0.071` n `23`; metal avg `-0.5639` n `20`; unknown avg `-0.1961` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
