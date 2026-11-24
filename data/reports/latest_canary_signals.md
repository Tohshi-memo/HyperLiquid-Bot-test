# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T11:37:24.814455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `0.0475` n `239`; crypto_major avg `0.1491` n `8`; equity avg `0.2102` n `166`; fx avg `0.0136` n `6`; index avg `0.0101` n `27`; metal avg `0.0257` n `20`; unknown avg `0.12` n `1266`
- 1h: commodity avg `-0.0292` n `13`; crypto_alt avg `-0.3861` n `239`; crypto_major avg `-0.0779` n `8`; equity avg `-0.3587` n `166`; fx avg `0.014` n `6`; index avg `-0.0663` n `27`; metal avg `0.0414` n `20`; unknown avg `158.7854` n `1262`
- 4h: commodity avg `0.0997` n `13`; crypto_alt avg `-1.8893` n `239`; crypto_major avg `-1.1959` n `8`; equity avg `-2.3611` n `166`; fx avg `0.1142` n `6`; index avg `-0.3086` n `27`; metal avg `-0.1285` n `20`; unknown avg `167.1412` n `1198`
- 24h: commodity avg `-0.3968` n `13`; crypto_alt avg `-1.7214` n `239`; crypto_major avg `-1.8393` n `8`; equity avg `0.8777` n `166`; fx avg `-0.0766` n `6`; index avg `0.2253` n `27`; metal avg `-0.3446` n `20`; unknown avg `-0.1362` n `1134`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
