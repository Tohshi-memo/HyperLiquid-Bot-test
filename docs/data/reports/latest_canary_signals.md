# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T18:37:32.738309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5406` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.531` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0688` n `13`; crypto_alt avg `-0.1599` n `239`; crypto_major avg `-0.2743` n `8`; equity avg `-0.0626` n `158`; fx avg `-0.0216` n `6`; index avg `-0.0243` n `27`; metal avg `-0.0434` n `20`; unknown avg `0.1373` n `1264`
- 1h: commodity avg `0.3757` n `13`; crypto_alt avg `-0.1494` n `239`; crypto_major avg `0.0441` n `8`; equity avg `-0.3803` n `158`; fx avg `-0.0213` n `6`; index avg `-0.0352` n `27`; metal avg `-0.0534` n `20`; unknown avg `4.8061` n `1258`
- 4h: commodity avg `-0.8725` n `13`; crypto_alt avg `0.9059` n `239`; crypto_major avg `1.6681` n `8`; equity avg `-0.8629` n `158`; fx avg `-0.0654` n `6`; index avg `0.0123` n `27`; metal avg `0.1971` n `20`; unknown avg `1.6971` n `1250`
- 24h: commodity avg `-1.5334` n `13`; crypto_alt avg `1.7107` n `239`; crypto_major avg `1.9847` n `8`; equity avg `-0.9219` n `158`; fx avg `0.0321` n `6`; index avg `0.0992` n `27`; metal avg `1.1878` n `20`; unknown avg `0.6008` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2712`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
