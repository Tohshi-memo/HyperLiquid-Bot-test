# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T16:22:34.605337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7509` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0528` n `13`; crypto_alt avg `-0.0589` n `237`; crypto_major avg `-0.0597` n `8`; equity avg `0.1235` n `151`; fx avg `0.0057` n `6`; index avg `0.0405` n `26`; metal avg `-0.0048` n `20`; unknown avg `7.9571` n `1233`
- 1h: commodity avg `0.139` n `13`; crypto_alt avg `0.0715` n `237`; crypto_major avg `0.1523` n `8`; equity avg `-0.5463` n `151`; fx avg `0.0315` n `6`; index avg `0.0297` n `26`; metal avg `-0.074` n `20`; unknown avg `5.0525` n `1225`
- 4h: commodity avg `-0.0652` n `13`; crypto_alt avg `-0.8343` n `237`; crypto_major avg `-0.1327` n `8`; equity avg `-1.8836` n `151`; fx avg `0.0639` n `6`; index avg `-0.0804` n `26`; metal avg `-0.1595` n `20`; unknown avg `2.8605` n `1083`
- 24h: commodity avg `0.4227` n `13`; crypto_alt avg `-4.7704` n `237`; crypto_major avg `-3.3561` n `8`; equity avg `-4.2886` n `151`; fx avg `-0.1358` n `6`; index avg `-0.5102` n `26`; metal avg `-0.9088` n `20`; unknown avg `6.5544` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
