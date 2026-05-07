# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T14:07:19.154106+00:00`
- Correlation status: `ready`
- Asset price records: `556`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4504` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `-0.0637` n `8`; equity avg `0.0553` n `65`; fx avg `-0.0051` n `5`; index avg `-0.0152` n `23`; metal avg `0.1034` n `18`; unknown avg `-0.2191` n `365`
- 1h: commodity avg `-0.2942` n `12`; crypto_alt avg `-0.8182` n `228`; crypto_major avg `-0.8368` n `8`; equity avg `-0.4354` n `65`; fx avg `-0.0076` n `5`; index avg `-0.3675` n `23`; metal avg `-0.2523` n `18`; unknown avg `-0.491` n `365`
- 4h: commodity avg `-1.033` n `12`; crypto_alt avg `-0.1817` n `228`; crypto_major avg `-0.8427` n `8`; equity avg `-0.5578` n `65`; fx avg `-0.0054` n `5`; index avg `-0.4361` n `23`; metal avg `0.105` n `18`; unknown avg `0.0442` n `365`
- 24h: commodity avg `-2.0972` n `12`; crypto_alt avg `1.7827` n `228`; crypto_major avg `-1.0037` n `8`; equity avg `1.5358` n `65`; fx avg `0.0978` n `5`; index avg `0.4644` n `23`; metal avg `1.7947` n `18`; unknown avg `0.3053` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `552`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `552`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0917`, n `552`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `552`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0819`, n `548`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `548`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `548`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `548`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `552`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `548`, weak_sample_signal
