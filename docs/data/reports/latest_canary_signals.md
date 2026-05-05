# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T12:00:30.544647+00:00`
- Correlation status: `ready`
- Asset price records: `358`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `7`; crypto_alt avg `0.0584` n `223`; crypto_major avg `-0.0194` n `7`; equity avg `0.053` n `47`; fx avg `0.0135` n `4`; index avg `0.0822` n `6`; metal avg `-0.0033` n `7`; unknown avg `0.1046` n `312`
- 1h: commodity avg `-0.2451` n `7`; crypto_alt avg `0.1177` n `223`; crypto_major avg `0.1182` n `7`; equity avg `0.1893` n `47`; fx avg `0.0201` n `4`; index avg `0.0416` n `6`; metal avg `0.4112` n `7`; unknown avg `0.0131` n `312`
- 4h: commodity avg `-0.2159` n `7`; crypto_alt avg `0.2959` n `223`; crypto_major avg `0.2939` n `7`; equity avg `0.4282` n `47`; fx avg `0.0822` n `4`; index avg `0.1483` n `6`; metal avg `0.345` n `7`; unknown avg `0.0726` n `312`
- 24h: commodity avg `0.2496` n `7`; crypto_alt avg `2.3935` n `223`; crypto_major avg `2.1695` n `7`; equity avg `0.6247` n `47`; fx avg `0.0811` n `4`; index avg `0.3788` n `6`; metal avg `0.8165` n `7`; unknown avg `-0.0603` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2141`, n `354`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2069`, n `354`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `354`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `354`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.116`, n `354`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `354`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `354`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `354`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `350`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0902`, n `350`, weak_sample_signal
