# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T11:00:37.749889+00:00`
- Correlation status: `ready`
- Asset price records: `354`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0853` n `7`; crypto_alt avg `0.0784` n `223`; crypto_major avg `0.1612` n `7`; equity avg `0.0102` n `47`; fx avg `-0.0035` n `4`; index avg `-0.019` n `6`; metal avg `-0.0484` n `7`; unknown avg `0.0164` n `312`
- 1h: commodity avg `0.1772` n `7`; crypto_alt avg `0.2827` n `223`; crypto_major avg `0.5213` n `7`; equity avg `0.0745` n `47`; fx avg `0.0177` n `4`; index avg `-0.0111` n `6`; metal avg `-0.3167` n `7`; unknown avg `0.1256` n `312`
- 4h: commodity avg `-0.0212` n `7`; crypto_alt avg `0.4769` n `223`; crypto_major avg `0.108` n `7`; equity avg `-0.0327` n `47`; fx avg `0.0751` n `4`; index avg `-0.011` n `6`; metal avg `0.0244` n `7`; unknown avg `0.5096` n `312`
- 24h: commodity avg `0.2779` n `7`; crypto_alt avg `2.3612` n `223`; crypto_major avg `1.9459` n `7`; equity avg `0.6897` n `47`; fx avg `0.0502` n `4`; index avg `0.3594` n `6`; metal avg `0.1726` n `7`; unknown avg `0.5065` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2169`, n `350`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2098`, n `350`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `350`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `350`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `350`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `350`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `350`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `350`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `346`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.098`, n `346`, weak_sample_signal
