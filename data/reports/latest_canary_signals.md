# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T02:00:27.862219+00:00`
- Correlation status: `ready`
- Asset price records: `412`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7286` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0564` n `7`; crypto_alt avg `0.3172` n `223`; crypto_major avg `0.1494` n `7`; equity avg `0.0855` n `47`; fx avg `-0.004` n `4`; index avg `0.0369` n `6`; metal avg `0.0777` n `7`; unknown avg `-0.084` n `313`
- 1h: commodity avg `-0.0894` n `7`; crypto_alt avg `1.0182` n `223`; crypto_major avg `0.5389` n `7`; equity avg `0.1823` n `47`; fx avg `-0.0222` n `4`; index avg `0.0119` n `6`; metal avg `0.4029` n `7`; unknown avg `-0.0181` n `313`
- 4h: commodity avg `-0.6183` n `7`; crypto_alt avg `0.7504` n `223`; crypto_major avg `-0.174` n `7`; equity avg `0.5515` n `47`; fx avg `-0.2969` n `4`; index avg `0.6565` n `6`; metal avg `1.5546` n `7`; unknown avg `-0.1441` n `313`
- 24h: commodity avg `-1.5834` n `7`; crypto_alt avg `2.67` n `223`; crypto_major avg `2.2886` n `7`; equity avg `2.8941` n `47`; fx avg `-0.2172` n `4`; index avg `2.3178` n `6`; metal avg `1.7809` n `7`; unknown avg `1.3372` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1864`, n `408`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1801`, n `408`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `408`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `408`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `408`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `408`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `404`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `408`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `408`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `404`, weak_sample_signal
