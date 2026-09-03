# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T12:07:28.860895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0654` n `232`; crypto_major avg `-0.0829` n `8`; equity avg `0.0575` n `133`; fx avg `-0.0079` n `6`; index avg `0.0179` n `26`; metal avg `0.0294` n `20`; unknown avg `0.5082` n `790`
- 1h: commodity avg `0.072` n `12`; crypto_alt avg `0.2947` n `232`; crypto_major avg `0.3851` n `8`; equity avg `-0.0899` n `133`; fx avg `-0.026` n `6`; index avg `-0.0064` n `26`; metal avg `0.1059` n `20`; unknown avg `2.0079` n `790`
- 4h: commodity avg `0.6119` n `12`; crypto_alt avg `-0.1093` n `232`; crypto_major avg `-0.0956` n `8`; equity avg `-0.4819` n `133`; fx avg `-0.0862` n `6`; index avg `-0.0977` n `26`; metal avg `-0.0902` n `20`; unknown avg `0.4165` n `790`
- 24h: commodity avg `0.857` n `12`; crypto_alt avg `2.2113` n `232`; crypto_major avg `2.1034` n `8`; equity avg `1.1246` n `133`; fx avg `-0.3779` n `6`; index avg `0.025` n `26`; metal avg `0.6083` n `20`; unknown avg `-0.3472` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
