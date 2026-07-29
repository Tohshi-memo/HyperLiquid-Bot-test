# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T13:52:31.292793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0832` n `12`; crypto_alt avg `-0.1143` n `230`; crypto_major avg `-0.0067` n `8`; equity avg `-1.0849` n `102`; fx avg `0.0077` n `6`; index avg `-0.1312` n `25`; metal avg `-0.0729` n `20`; unknown avg `-0.04` n `777`
- 1h: commodity avg `0.1156` n `12`; crypto_alt avg `0.0812` n `230`; crypto_major avg `0.0038` n `8`; equity avg `-1.2391` n `102`; fx avg `0.0009` n `6`; index avg `-0.0896` n `25`; metal avg `-0.0591` n `20`; unknown avg `0.6435` n `777`
- 4h: commodity avg `0.5932` n `12`; crypto_alt avg `-0.5345` n `230`; crypto_major avg `-0.5199` n `8`; equity avg `-1.8824` n `102`; fx avg `0.0157` n `6`; index avg `-0.1973` n `25`; metal avg `-0.2342` n `20`; unknown avg `0.5539` n `777`
- 24h: commodity avg `0.5972` n `12`; crypto_alt avg `-1.0892` n `230`; crypto_major avg `1.3004` n `8`; equity avg `0.3709` n `102`; fx avg `-0.0895` n `6`; index avg `-0.1243` n `25`; metal avg `-0.0784` n `20`; unknown avg `0.1135` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
