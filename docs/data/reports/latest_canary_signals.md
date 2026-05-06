# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T03:30:32.065976+00:00`
- Correlation status: `ready`
- Asset price records: `418`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `7`; crypto_alt avg `0.2351` n `223`; crypto_major avg `0.2624` n `7`; equity avg `0.0766` n `47`; fx avg `0.0236` n `4`; index avg `0.0112` n `6`; metal avg `-0.093` n `7`; unknown avg `-0.095` n `313`
- 1h: commodity avg `0.1019` n `7`; crypto_alt avg `0.5323` n `223`; crypto_major avg `0.5673` n `7`; equity avg `0.2613` n `47`; fx avg `0.029` n `4`; index avg `0.0059` n `6`; metal avg `0.4808` n `7`; unknown avg `0.228` n `313`
- 4h: commodity avg `0.2096` n `7`; crypto_alt avg `1.411` n `223`; crypto_major avg `0.7519` n `7`; equity avg `0.4506` n `47`; fx avg `-0.254` n `4`; index avg `0.4213` n `6`; metal avg `1.3089` n `7`; unknown avg `0.3228` n `313`
- 24h: commodity avg `-1.417` n `7`; crypto_alt avg `2.5041` n `223`; crypto_major avg `2.0955` n `7`; equity avg `2.9626` n `47`; fx avg `-0.1518` n `4`; index avg `2.1473` n `6`; metal avg `2.1756` n `7`; unknown avg `1.4766` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1821`, n `414`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1758`, n `414`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `414`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `414`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `414`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `414`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1`, n `410`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `414`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `414`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0938`, n `410`, weak_sample_signal
