# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T03:07:13.487317+00:00`
- Correlation status: `ready`
- Asset price records: `608`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0637` n `12`; crypto_alt avg `-0.442` n `228`; crypto_major avg `-0.3218` n `8`; equity avg `0.0843` n `65`; fx avg `0.0009` n `5`; index avg `-0.018` n `23`; metal avg `-0.0262` n `18`; unknown avg `0.9988` n `365`
- 1h: commodity avg `-0.1537` n `12`; crypto_alt avg `0.0378` n `228`; crypto_major avg `-0.1289` n `8`; equity avg `0.0277` n `65`; fx avg `-0.0052` n `5`; index avg `-0.0535` n `23`; metal avg `-0.256` n `18`; unknown avg `1.7156` n `365`
- 4h: commodity avg `-0.5243` n `12`; crypto_alt avg `-0.3892` n `228`; crypto_major avg `-0.5914` n `8`; equity avg `0.5554` n `65`; fx avg `0.112` n `5`; index avg `0.3365` n `23`; metal avg `0.788` n `18`; unknown avg `0.9171` n `365`
- 24h: commodity avg `0.3985` n `12`; crypto_alt avg `1.6041` n `228`; crypto_major avg `-1.5223` n `8`; equity avg `-0.9249` n `65`; fx avg `0.1711` n `5`; index avg `-0.6292` n `23`; metal avg `0.1527` n `18`; unknown avg `0.9012` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1319`, n `604`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `604`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `604`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `604`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1106`, n `600`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1091`, n `600`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `600`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.09`, n `600`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0792`, n `600`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `604`, weak_sample_signal
