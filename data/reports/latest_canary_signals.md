# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T09:02:40.409242+00:00`
- Correlation status: `ready`
- Asset price records: `346`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `7`; crypto_alt avg `-0.045` n `223`; crypto_major avg `0.0003` n `7`; equity avg `-0.0472` n `47`; fx avg `0.0196` n `4`; index avg `-0.1468` n `6`; metal avg `0.0698` n `7`; unknown avg `0.0204` n `312`
- 1h: commodity avg `-0.2637` n `7`; crypto_alt avg `-0.1153` n `223`; crypto_major avg `-0.1568` n `7`; equity avg `0.2477` n `47`; fx avg `0.0214` n `4`; index avg `0.0736` n `6`; metal avg `0.1853` n `7`; unknown avg `-0.2846` n `312`
- 4h: commodity avg `-0.2047` n `7`; crypto_alt avg `0.5129` n `223`; crypto_major avg `0.2587` n `7`; equity avg `0.6014` n `47`; fx avg `0.0357` n `4`; index avg `0.2206` n `6`; metal avg `0.7732` n `7`; unknown avg `0.4137` n `310`
- 24h: commodity avg `0.3588` n `7`; crypto_alt avg `1.1045` n `223`; crypto_major avg `0.6296` n `7`; equity avg `0.0704` n `47`; fx avg `0.0003` n `4`; index avg `-0.0536` n `6`; metal avg `-0.0123` n `7`; unknown avg `-0.8047` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2181`, n `342`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.211`, n `342`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `342`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `342`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1176`, n `342`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `342`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `342`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `342`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `338`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `338`, weak_sample_signal
