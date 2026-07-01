# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T07:07:36.451584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.2679` n `228`; crypto_major avg `-0.2368` n `8`; equity avg `-0.2076` n `88`; fx avg `-0.015` n `6`; index avg `-0.0226` n `23`; metal avg `-0.1078` n `20`; unknown avg `-0.0533` n `763`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `-0.8184` n `228`; crypto_major avg `-0.8147` n `8`; equity avg `-0.2721` n `88`; fx avg `0.0161` n `6`; index avg `-0.037` n `23`; metal avg `-0.0862` n `20`; unknown avg `-0.0942` n `763`
- 4h: commodity avg `-0.1291` n `12`; crypto_alt avg `-0.5403` n `228`; crypto_major avg `-0.9274` n `8`; equity avg `-0.3469` n `88`; fx avg `-0.0259` n `6`; index avg `-0.0551` n `23`; metal avg `-0.3099` n `20`; unknown avg `0.2333` n `743`
- 24h: commodity avg `-0.066` n `12`; crypto_alt avg `-1.2227` n `228`; crypto_major avg `-1.0209` n `8`; equity avg `0.1618` n `88`; fx avg `0.1001` n `6`; index avg `-0.0785` n `23`; metal avg `-0.9609` n `20`; unknown avg `-0.1687` n `743`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
