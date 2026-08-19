# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:03:55.828685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `-0.0754` n `230`; crypto_major avg `-0.0517` n `8`; equity avg `-0.0962` n `120`; fx avg `-0.001` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.5389` n `789`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.2806` n `230`; crypto_major avg `0.1419` n `8`; equity avg `-0.1767` n `120`; fx avg `0.0064` n `6`; index avg `-0.017` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.042` n `789`
- 4h: commodity avg `0.0483` n `12`; crypto_alt avg `0.1938` n `230`; crypto_major avg `-0.1164` n `8`; equity avg `0.5012` n `120`; fx avg `-0.1461` n `6`; index avg `0.0144` n `25`; metal avg `0.0816` n `20`; unknown avg `0.3625` n `789`
- 24h: commodity avg `0.2893` n `12`; crypto_alt avg `0.7345` n `230`; crypto_major avg `0.3301` n `8`; equity avg `-3.1631` n `120`; fx avg `-0.1435` n `6`; index avg `-0.5121` n `25`; metal avg `-0.5117` n `20`; unknown avg `-0.1153` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
