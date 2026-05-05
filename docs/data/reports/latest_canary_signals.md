# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T07:00:29.167706+00:00`
- Correlation status: `ready`
- Asset price records: `338`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `7`; crypto_alt avg `0.1703` n `223`; crypto_major avg `0.3167` n `7`; equity avg `0.1559` n `47`; fx avg `-0.0064` n `4`; index avg `0.0547` n `6`; metal avg `0.0967` n `7`; unknown avg `0.0509` n `312`
- 1h: commodity avg `0.1` n `7`; crypto_alt avg `-0.0277` n `223`; crypto_major avg `0.1537` n `7`; equity avg `0.2198` n `47`; fx avg `-0.0055` n `4`; index avg `0.1444` n `6`; metal avg `-0.002` n `7`; unknown avg `0.004` n `312`
- 4h: commodity avg `0.1767` n `7`; crypto_alt avg `0.2543` n `223`; crypto_major avg `0.8023` n `7`; equity avg `0.7473` n `47`; fx avg `-0.0074` n `4`; index avg `0.4067` n `6`; metal avg `0.2445` n `7`; unknown avg `1.4578` n `310`
- 24h: commodity avg `0.838` n `7`; crypto_alt avg `0.8283` n `223`; crypto_major avg `0.729` n `7`; equity avg `0.0081` n `47`; fx avg `-0.0441` n `4`; index avg `-0.0747` n `6`; metal avg `-0.8973` n `7`; unknown avg `1.1109` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2221`, n `334`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2154`, n `334`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1395`, n `334`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.135`, n `334`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.132`, n `334`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `334`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `334`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `334`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1059`, n `330`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1009`, n `330`, weak_sample_signal
