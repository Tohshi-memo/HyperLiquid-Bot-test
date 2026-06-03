# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T05:15:43.762458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.
- 1h_crypto_metal_divergence: score `1.626` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `0.3756` n `228`; crypto_major avg `0.2901` n `8`; equity avg `0.1524` n `72`; fx avg `0.0005` n `6`; index avg `0.0304` n `23`; metal avg `0.1356` n `18`; unknown avg `2.192` n `420`
- 1h: commodity avg `-0.072` n `12`; crypto_alt avg `2.1021` n `228`; crypto_major avg `1.4734` n `8`; equity avg `0.2191` n `72`; fx avg `-0.016` n `6`; index avg `0.0145` n `23`; metal avg `-0.1526` n `18`; unknown avg `2.1167` n `420`
- 4h: commodity avg `-0.1492` n `12`; crypto_alt avg `1.6584` n `228`; crypto_major avg `0.8461` n `8`; equity avg `0.3907` n `72`; fx avg `-0.0007` n `6`; index avg `0.0008` n `23`; metal avg `0.1989` n `18`; unknown avg `-0.0122` n `419`
- 24h: commodity avg `0.9681` n `12`; crypto_alt avg `-2.2841` n `228`; crypto_major avg `-4.2953` n `8`; equity avg `1.1236` n `72`; fx avg `0.0368` n `6`; index avg `1.3049` n `23`; metal avg `-0.6085` n `18`; unknown avg `-0.7102` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
