# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T06:07:26.110516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.1287` n `228`; crypto_major avg `-0.1159` n `8`; equity avg `-0.3058` n `88`; fx avg `-0.0179` n `6`; index avg `-0.0765` n `25`; metal avg `0.1335` n `20`; unknown avg `-0.2343` n `741`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.4393` n `228`; crypto_major avg `-0.4692` n `8`; equity avg `-0.6604` n `88`; fx avg `-0.0019` n `6`; index avg `-0.2013` n `25`; metal avg `0.1052` n `20`; unknown avg `-0.0967` n `741`
- 4h: commodity avg `-0.026` n `12`; crypto_alt avg `0.1465` n `228`; crypto_major avg `0.2709` n `8`; equity avg `-1.0961` n `88`; fx avg `-0.0137` n `6`; index avg `-0.3056` n `25`; metal avg `0.2387` n `20`; unknown avg `-0.228` n `739`
- 24h: commodity avg `-0.5315` n `12`; crypto_alt avg `1.4957` n `228`; crypto_major avg `0.981` n `8`; equity avg `-1.9848` n `88`; fx avg `0.0045` n `6`; index avg `-0.5199` n `25`; metal avg `1.2929` n `20`; unknown avg `24.9747` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
