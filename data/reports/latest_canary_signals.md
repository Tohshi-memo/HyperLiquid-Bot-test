# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T06:00:28.243729+00:00`
- Correlation status: `ready`
- Asset price records: `334`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `7`; crypto_alt avg `0.1388` n `223`; crypto_major avg `0.0655` n `7`; equity avg `-0.0321` n `47`; fx avg `0.0072` n `4`; index avg `0.0325` n `6`; metal avg `0.0819` n `7`; unknown avg `-0.0447` n `310`
- 1h: commodity avg `0.0101` n `7`; crypto_alt avg `0.3568` n `223`; crypto_major avg `0.3292` n `7`; equity avg `0.451` n `47`; fx avg `0.0067` n `4`; index avg `0.1205` n `6`; metal avg `0.4983` n `7`; unknown avg `1.2132` n `310`
- 4h: commodity avg `-0.0843` n `7`; crypto_alt avg `0.3201` n `223`; crypto_major avg `0.8338` n `7`; equity avg `0.7844` n `47`; fx avg `-0.0024` n `4`; index avg `0.2865` n `6`; metal avg `0.3939` n `7`; unknown avg `1.4622` n `310`
- 24h: commodity avg `1.2427` n `7`; crypto_alt avg `0.6114` n `223`; crypto_major avg `0.0532` n `7`; equity avg `-0.3147` n `47`; fx avg `-0.0225` n `4`; index avg `-0.1284` n `6`; metal avg `-1.2136` n `7`; unknown avg `0.1168` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2223`, n `330`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2156`, n `330`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `330`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `330`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.134`, n `330`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `330`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `330`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1075`, n `326`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `330`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `330`, weak_sample_signal
