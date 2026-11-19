# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T19:22:30.816293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8905` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.071` n `13`; crypto_alt avg `0.1931` n `239`; crypto_major avg `0.1352` n `8`; equity avg `0.4644` n `165`; fx avg `-0.0023` n `6`; index avg `0.0478` n `27`; metal avg `0.0385` n `20`; unknown avg `7.6178` n `1260`
- 1h: commodity avg `-0.1482` n `13`; crypto_alt avg `-0.0119` n `239`; crypto_major avg `-0.4752` n `8`; equity avg `0.0132` n `165`; fx avg `-0.0069` n `6`; index avg `0.0067` n `27`; metal avg `0.0098` n `20`; unknown avg `3.0388` n `1260`
- 4h: commodity avg `-0.1173` n `13`; crypto_alt avg `-0.8077` n `239`; crypto_major avg `-0.5834` n `8`; equity avg `-2.4739` n `165`; fx avg `0.0068` n `6`; index avg `-0.2699` n `27`; metal avg `-0.1838` n `20`; unknown avg `12.7575` n `1253`
- 24h: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.3222` n `239`; crypto_major avg `0.2672` n `8`; equity avg `-1.1226` n `165`; fx avg `-0.0077` n `6`; index avg `-0.0385` n `27`; metal avg `-0.4345` n `20`; unknown avg `6.3841` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
