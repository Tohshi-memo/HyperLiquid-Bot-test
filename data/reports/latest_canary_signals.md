# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T14:22:33.256162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `-0.0712` n `230`; crypto_major avg `-0.1225` n `8`; equity avg `-0.4304` n `102`; fx avg `-0.0145` n `6`; index avg `-0.0548` n `25`; metal avg `0.0646` n `20`; unknown avg `-0.0091` n `777`
- 1h: commodity avg `0.1328` n `12`; crypto_alt avg `0.041` n `230`; crypto_major avg `0.024` n `8`; equity avg `-1.1161` n `102`; fx avg `-0.0014` n `6`; index avg `-0.1152` n `25`; metal avg `-0.0528` n `20`; unknown avg `0.3498` n `777`
- 4h: commodity avg `0.4223` n `12`; crypto_alt avg `-0.5333` n `230`; crypto_major avg `-0.524` n `8`; equity avg `-1.7348` n `102`; fx avg `0.0116` n `6`; index avg `-0.2008` n `25`; metal avg `-0.1232` n `20`; unknown avg `0.4536` n `777`
- 24h: commodity avg `0.6668` n `12`; crypto_alt avg `-1.0094` n `230`; crypto_major avg `1.3549` n `8`; equity avg `0.8561` n `102`; fx avg `-0.0747` n `6`; index avg `-0.0248` n `25`; metal avg `0.0065` n `20`; unknown avg `0.0481` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
