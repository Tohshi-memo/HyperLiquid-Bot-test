# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T20:07:33.391815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `1.5344` n `228`; crypto_major avg `1.372` n `8`; equity avg `1.1724` n `86`; fx avg `-0.0006` n `6`; index avg `0.2653` n `23`; metal avg `0.2995` n `20`; unknown avg `3.8275` n `764`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `1.7482` n `228`; crypto_major avg `1.5184` n `8`; equity avg `1.707` n `86`; fx avg `-0.0172` n `6`; index avg `0.3965` n `23`; metal avg `0.4176` n `20`; unknown avg `1.4698` n `764`
- 4h: commodity avg `-0.0364` n `12`; crypto_alt avg `0.0649` n `228`; crypto_major avg `0.4162` n `8`; equity avg `0.1778` n `86`; fx avg `0.0198` n `6`; index avg `0.1631` n `23`; metal avg `-0.1741` n `20`; unknown avg `-0.1516` n `764`
- 24h: commodity avg `-0.6022` n `12`; crypto_alt avg `-2.7179` n `228`; crypto_major avg `-2.5732` n `8`; equity avg `3.2082` n `86`; fx avg `0.0564` n `6`; index avg `0.3487` n `23`; metal avg `-1.6369` n `20`; unknown avg `-0.5487` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
