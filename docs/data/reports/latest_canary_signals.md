# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T05:00:24.892751+00:00`
- Correlation status: `ready`
- Asset price records: `424`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `7`; crypto_alt avg `-0.1328` n `223`; crypto_major avg `-0.1` n `7`; equity avg `-0.0968` n `47`; fx avg `0.0689` n `4`; index avg `-0.0392` n `6`; metal avg `0.0067` n `7`; unknown avg `0.0143` n `313`
- 1h: commodity avg `-0.0697` n `7`; crypto_alt avg `-0.4135` n `223`; crypto_major avg `-0.3669` n `7`; equity avg `0.0144` n `47`; fx avg `-0.256` n `4`; index avg `0.0968` n `6`; metal avg `0.0116` n `7`; unknown avg `-0.0361` n `313`
- 4h: commodity avg `-0.0799` n `7`; crypto_alt avg `0.8004` n `223`; crypto_major avg `0.4817` n `7`; equity avg `0.6638` n `47`; fx avg `-0.2339` n `4`; index avg `0.1854` n `6`; metal avg `0.9182` n `7`; unknown avg `0.1893` n `313`
- 24h: commodity avg `-1.4829` n `7`; crypto_alt avg `2.4883` n `223`; crypto_major avg `1.7199` n `7`; equity avg `3.0833` n `47`; fx avg `-0.42` n `4`; index avg `2.3277` n `6`; metal avg `2.4115` n `7`; unknown avg `1.3124` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1809`, n `420`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1746`, n `420`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1279`, n `420`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `420`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `420`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `420`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1013`, n `416`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `416`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `420`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `420`, weak_sample_signal
