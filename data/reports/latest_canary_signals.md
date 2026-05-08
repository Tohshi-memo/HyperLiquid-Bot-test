# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T04:43:29.500636+00:00`
- Correlation status: `ready`
- Asset price records: `614`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `-0.1974` n `228`; crypto_major avg `-0.2504` n `8`; equity avg `-0.0345` n `65`; fx avg `0.0119` n `5`; index avg `-0.0342` n `23`; metal avg `-0.2016` n `18`; unknown avg `0.1232` n `365`
- 1h: commodity avg `0.3042` n `12`; crypto_alt avg `0.0727` n `228`; crypto_major avg `-0.2167` n `8`; equity avg `0.1338` n `65`; fx avg `0.0527` n `5`; index avg `-0.0188` n `23`; metal avg `-0.3354` n `18`; unknown avg `-0.2611` n `365`
- 4h: commodity avg `-0.3033` n `12`; crypto_alt avg `0.0453` n `228`; crypto_major avg `-0.5394` n `8`; equity avg `0.1875` n `65`; fx avg `0.0789` n `5`; index avg `0.146` n `23`; metal avg `0.4363` n `18`; unknown avg `-0.3101` n `365`
- 24h: commodity avg `0.5549` n `12`; crypto_alt avg `1.9011` n `228`; crypto_major avg `-1.4318` n `8`; equity avg `-0.9214` n `65`; fx avg `0.2276` n `5`; index avg `-0.6025` n `23`; metal avg `0.33` n `18`; unknown avg `-0.0951` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `610`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.117`, n `606`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `610`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1162`, n `606`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `610`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `610`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `606`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `606`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0789`, n `606`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `610`, weak_sample_signal
