# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T07:45:35.470748+00:00`
- Correlation status: `ready`
- Asset price records: `435`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1584` n `7`; crypto_alt avg `0.012` n `223`; crypto_major avg `0.0219` n `7`; equity avg `0.0181` n `47`; fx avg `-0.0416` n `4`; index avg `-0.0932` n `6`; metal avg `0.1474` n `7`; unknown avg `0.0731` n `313`
- 1h: commodity avg `-0.2639` n `7`; crypto_alt avg `0.441` n `223`; crypto_major avg `0.3415` n `7`; equity avg `0.0022` n `47`; fx avg `0.0101` n `4`; index avg `-0.2169` n `6`; metal avg `0.159` n `7`; unknown avg `1.3819` n `313`
- 4h: commodity avg `-0.1135` n `7`; crypto_alt avg `0.589` n `223`; crypto_major avg `0.4108` n `7`; equity avg `0.2726` n `47`; fx avg `-0.23` n `4`; index avg `-0.0391` n `6`; metal avg `0.2968` n `7`; unknown avg `2.0549` n `311`
- 24h: commodity avg `-1.4669` n `7`; crypto_alt avg `2.7387` n `223`; crypto_major avg `1.9107` n `7`; equity avg `2.5485` n `47`; fx avg `-0.404` n `4`; index avg `1.9732` n `6`; metal avg `1.8985` n `7`; unknown avg `1.957` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1804`, n `431`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1742`, n `431`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1264`, n `431`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `431`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.121`, n `431`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `431`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.098`, n `427`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `431`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.093`, n `427`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `431`, weak_sample_signal
