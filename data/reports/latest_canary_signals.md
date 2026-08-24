# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:42:46.502881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.0254` n `231`; crypto_major avg `-0.0694` n `8`; equity avg `-0.0247` n `122`; fx avg `-0.0103` n `6`; index avg `0.0026` n `25`; metal avg `0.0282` n `20`; unknown avg `-0.0401` n `794`
- 1h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.2926` n `231`; crypto_major avg `0.0207` n `8`; equity avg `-0.039` n `122`; fx avg `0.0017` n `6`; index avg `0.0022` n `25`; metal avg `0.066` n `20`; unknown avg `-0.1683` n `794`
- 4h: commodity avg `-0.0614` n `12`; crypto_alt avg `0.0917` n `231`; crypto_major avg `0.4947` n `8`; equity avg `-0.4193` n `122`; fx avg `-0.0077` n `6`; index avg `-0.0765` n `25`; metal avg `0.191` n `20`; unknown avg `-0.5565` n `794`
- 24h: commodity avg `-0.1629` n `12`; crypto_alt avg `-1.6778` n `231`; crypto_major avg `-0.9186` n `8`; equity avg `-2.7623` n `122`; fx avg `-0.0727` n `6`; index avg `-0.3188` n `25`; metal avg `0.1739` n `20`; unknown avg `0.7608` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
