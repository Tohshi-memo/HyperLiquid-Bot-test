# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T06:22:26.473534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.1672` n `233`; crypto_major avg `-0.1155` n `8`; equity avg `-0.0094` n `136`; fx avg `0.0001` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0902` n `838`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `-0.1644` n `233`; crypto_major avg `-0.1195` n `8`; equity avg `-0.1459` n `136`; fx avg `-0.0024` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.1208` n `812`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `0.1084` n `233`; crypto_major avg `-0.1711` n `8`; equity avg `-0.2931` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0602` n `26`; metal avg `0.0016` n `20`; unknown avg `-0.0278` n `804`
- 24h: commodity avg `0.1738` n `12`; crypto_alt avg `0.8801` n `233`; crypto_major avg `0.0652` n `8`; equity avg `-0.6532` n `136`; fx avg `-0.0054` n `6`; index avg `-0.1052` n `26`; metal avg `0.0317` n `20`; unknown avg `0.4678` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
