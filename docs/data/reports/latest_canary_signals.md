# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T19:52:34.488085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8252` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `0.0453` n `239`; crypto_major avg `-0.038` n `8`; equity avg `-0.2945` n `165`; fx avg `-0.0045` n `6`; index avg `-0.0563` n `27`; metal avg `-0.0652` n `20`; unknown avg `1.3204` n `1262`
- 1h: commodity avg `-0.0497` n `13`; crypto_alt avg `-0.0992` n `239`; crypto_major avg `-0.7207` n `8`; equity avg `-0.2827` n `165`; fx avg `-0.0192` n `6`; index avg `-0.0298` n `27`; metal avg `-0.0871` n `20`; unknown avg `2.2512` n `1260`
- 4h: commodity avg `-0.0257` n `13`; crypto_alt avg `-0.0989` n `239`; crypto_major avg `-0.0509` n `8`; equity avg `-1.8761` n `165`; fx avg `-0.055` n `6`; index avg `-0.1785` n `27`; metal avg `-0.1223` n `20`; unknown avg `12.0899` n `1253`
- 24h: commodity avg `-0.1588` n `13`; crypto_alt avg `0.0479` n `239`; crypto_major avg `0.3278` n `8`; equity avg `-1.0405` n `165`; fx avg `0.003` n `6`; index avg `-0.044` n `27`; metal avg `-0.4514` n `20`; unknown avg `6.7038` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
