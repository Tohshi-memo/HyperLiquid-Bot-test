# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T21:22:27.680422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0464` n `231`; crypto_major avg `0.0272` n `8`; equity avg `0.0242` n `122`; fx avg `-0.0148` n `6`; index avg `0.0012` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.074` n `794`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.5286` n `231`; crypto_major avg `0.508` n `8`; equity avg `0.1191` n `122`; fx avg `-0.0211` n `6`; index avg `0.0056` n `25`; metal avg `0.0053` n `20`; unknown avg `-0.1001` n `794`
- 4h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.5047` n `231`; crypto_major avg `0.5911` n `8`; equity avg `-0.1868` n `122`; fx avg `-0.0248` n `6`; index avg `-0.0169` n `25`; metal avg `0.037` n `20`; unknown avg `-0.5192` n `794`
- 24h: commodity avg `-0.2138` n `12`; crypto_alt avg `-2.1065` n `231`; crypto_major avg `-1.2648` n `8`; equity avg `-2.8527` n `122`; fx avg `-0.0573` n `6`; index avg `-0.3615` n `25`; metal avg `0.0849` n `20`; unknown avg `0.8785` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
