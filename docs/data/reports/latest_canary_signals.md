# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T04:52:28.135871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0977` n `232`; crypto_major avg `-0.0553` n `8`; equity avg `0.1057` n `128`; fx avg `0.0047` n `6`; index avg `0.0231` n `26`; metal avg `0.0038` n `20`; unknown avg `-0.2376` n `793`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.3507` n `232`; crypto_major avg `-0.4061` n `8`; equity avg `0.1817` n `128`; fx avg `0.0148` n `6`; index avg `0.0662` n `26`; metal avg `0.0179` n `20`; unknown avg `-0.3007` n `791`
- 4h: commodity avg `0.2574` n `12`; crypto_alt avg `0.0872` n `231`; crypto_major avg `-0.5998` n `8`; equity avg `-0.095` n `128`; fx avg `-0.0686` n `6`; index avg `0.0712` n `26`; metal avg `-0.3065` n `20`; unknown avg `-0.672` n `779`
- 24h: commodity avg `0.3745` n `12`; crypto_alt avg `-0.1515` n `231`; crypto_major avg `-1.9878` n `8`; equity avg `-0.9825` n `128`; fx avg `-0.0451` n `6`; index avg `-0.1565` n `26`; metal avg `-0.3541` n `20`; unknown avg `-0.5048` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
