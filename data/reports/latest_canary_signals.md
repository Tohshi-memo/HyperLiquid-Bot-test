# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T18:22:32.129854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `0.3715` n `234`; crypto_major avg `0.3729` n `8`; equity avg `0.0428` n `141`; fx avg `0.0032` n `6`; index avg `0.0126` n `26`; metal avg `0.0212` n `20`; unknown avg `0.4275` n `960`
- 1h: commodity avg `0.1296` n `12`; crypto_alt avg `0.4484` n `234`; crypto_major avg `0.4029` n `8`; equity avg `-0.0617` n `141`; fx avg `-0.0114` n `6`; index avg `0.0157` n `26`; metal avg `-0.0032` n `20`; unknown avg `1.259` n `958`
- 4h: commodity avg `-0.1169` n `12`; crypto_alt avg `1.0608` n `234`; crypto_major avg `0.3629` n `8`; equity avg `0.5482` n `141`; fx avg `-0.036` n `6`; index avg `0.1697` n `26`; metal avg `0.2501` n `20`; unknown avg `4.716` n `930`
- 24h: commodity avg `-0.7643` n `12`; crypto_alt avg `2.4173` n `234`; crypto_major avg `0.8352` n `8`; equity avg `0.3142` n `141`; fx avg `-0.256` n `6`; index avg `0.2375` n `26`; metal avg `0.1626` n `20`; unknown avg `1596.7799` n `807`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
