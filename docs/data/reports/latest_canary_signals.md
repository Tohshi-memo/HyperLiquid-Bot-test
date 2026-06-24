# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T00:22:25.577222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0623` n `12`; crypto_alt avg `0.0865` n `228`; crypto_major avg `0.1015` n `8`; equity avg `0.186` n `86`; fx avg `0.0063` n `6`; index avg `0.0675` n `23`; metal avg `-0.0936` n `20`; unknown avg `-0.0675` n `764`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.3743` n `228`; crypto_major avg `0.4244` n `8`; equity avg `0.595` n `86`; fx avg `0.052` n `6`; index avg `0.1444` n `23`; metal avg `0.0437` n `20`; unknown avg `0.218` n `764`
- 4h: commodity avg `-0.0883` n `12`; crypto_alt avg `0.2347` n `228`; crypto_major avg `0.4819` n `8`; equity avg `0.4137` n `86`; fx avg `0.0285` n `6`; index avg `0.1883` n `23`; metal avg `-0.0482` n `20`; unknown avg `0.1504` n `756`
- 24h: commodity avg `-0.4336` n `12`; crypto_alt avg `-1.5588` n `228`; crypto_major avg `-2.4657` n `8`; equity avg `-2.1596` n `86`; fx avg `-0.1702` n `6`; index avg `-0.5653` n `23`; metal avg `-1.0528` n `20`; unknown avg `0.6738` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
