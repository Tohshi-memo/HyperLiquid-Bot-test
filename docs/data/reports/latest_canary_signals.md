# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T08:00:36.745697+00:00`
- Correlation status: `ready`
- Asset price records: `342`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2144` n `7`; crypto_alt avg `-0.0623` n `223`; crypto_major avg `-0.0926` n `7`; equity avg `-0.2474` n `47`; fx avg `-0.0009` n `4`; index avg `-0.0328` n `6`; metal avg `-0.1356` n `7`; unknown avg `0.189` n `312`
- 1h: commodity avg `-0.0501` n `7`; crypto_alt avg `0.3148` n `223`; crypto_major avg `-0.0674` n `7`; equity avg `-0.2584` n `47`; fx avg `0.0131` n `4`; index avg `-0.1172` n `6`; metal avg `0.0899` n `7`; unknown avg `0.4534` n `312`
- 4h: commodity avg `-0.0108` n `7`; crypto_alt avg `0.4454` n `223`; crypto_major avg `0.2901` n `7`; equity avg `0.4452` n `47`; fx avg `0.0051` n `4`; index avg `0.2093` n `6`; metal avg `0.5366` n `7`; unknown avg `1.805` n `310`
- 24h: commodity avg `0.4234` n `7`; crypto_alt avg `1.2501` n `223`; crypto_major avg `0.6519` n `7`; equity avg `-0.3347` n `47`; fx avg `-0.0071` n `4`; index avg `-0.2004` n `6`; metal avg `-0.2895` n `7`; unknown avg `0.2104` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2188`, n `338`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2118`, n `338`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `338`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1341`, n `338`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.119`, n `338`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `338`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `338`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `338`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `334`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.093`, n `334`, weak_sample_signal
