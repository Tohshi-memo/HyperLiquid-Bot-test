# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T06:37:29.187866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1596` n `12`; crypto_alt avg `0.0494` n `230`; crypto_major avg `0.1368` n `8`; equity avg `0.051` n `102`; fx avg `0.0017` n `6`; index avg `0.0014` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0094` n `774`
- 1h: commodity avg `-0.166` n `12`; crypto_alt avg `0.1686` n `230`; crypto_major avg `0.0301` n `8`; equity avg `-0.0689` n `102`; fx avg `-0.001` n `6`; index avg `0.0301` n `25`; metal avg `0.1029` n `20`; unknown avg `-0.0055` n `758`
- 4h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.1609` n `230`; crypto_major avg `0.0291` n `8`; equity avg `-0.3731` n `102`; fx avg `-0.0298` n `6`; index avg `-0.0596` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.0381` n `758`
- 24h: commodity avg `-0.5793` n `12`; crypto_alt avg `-3.8886` n `230`; crypto_major avg `-3.8547` n `8`; equity avg `-4.1647` n `102`; fx avg `-0.2006` n `6`; index avg `-0.883` n `25`; metal avg `-0.4149` n `20`; unknown avg `1161.4796` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
