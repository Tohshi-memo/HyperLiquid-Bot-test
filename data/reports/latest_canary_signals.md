# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T21:07:33.619833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `0.2921` n `231`; crypto_major avg `0.2815` n `8`; equity avg `0.0731` n `122`; fx avg `-0.0084` n `6`; index avg `0.0103` n `25`; metal avg `0.0165` n `20`; unknown avg `0.5065` n `794`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.5171` n `231`; crypto_major avg `0.4176` n `8`; equity avg `0.0585` n `122`; fx avg `-0.0074` n `6`; index avg `0.0014` n `25`; metal avg `0.0154` n `20`; unknown avg `0.5607` n `794`
- 4h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.2513` n `231`; crypto_major avg `-0.3041` n `8`; equity avg `-0.4025` n `122`; fx avg `-0.0078` n `6`; index avg `-0.037` n `25`; metal avg `-0.0217` n `20`; unknown avg `-0.0502` n `794`
- 24h: commodity avg `-0.2262` n `12`; crypto_alt avg `-1.6135` n `231`; crypto_major avg `-0.822` n `8`; equity avg `-2.8164` n `122`; fx avg `-0.074` n `6`; index avg `-0.3598` n `25`; metal avg `0.0874` n `20`; unknown avg `1.0785` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
