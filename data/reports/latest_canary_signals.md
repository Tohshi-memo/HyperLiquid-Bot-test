# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T15:07:17.288819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.008` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.3264` n `12`; crypto_alt avg `-0.3857` n `228`; crypto_major avg `-0.4816` n `8`; equity avg `-0.1159` n `66`; fx avg `0.004` n `5`; index avg `-0.1115` n `23`; metal avg `-0.239` n `18`; unknown avg `1.0669` n `384`
- 1h: commodity avg `0.876` n `12`; crypto_alt avg `-1.0684` n `228`; crypto_major avg `-1.132` n `8`; equity avg `-1.1391` n `66`; fx avg `0.0107` n `5`; index avg `-0.3962` n `23`; metal avg `-0.5131` n `18`; unknown avg `-0.4891` n `384`
- 4h: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.1818` n `228`; crypto_major avg `-0.5934` n `8`; equity avg `-0.9407` n `66`; fx avg `-0.0301` n `5`; index avg `-0.2524` n `23`; metal avg `0.2888` n `18`; unknown avg `1.1475` n `383`
- 24h: commodity avg `0.9306` n `12`; crypto_alt avg `-3.1722` n `228`; crypto_major avg `-2.5452` n `8`; equity avg `-0.5307` n `66`; fx avg `0.0548` n `5`; index avg `-0.2693` n `23`; metal avg `0.1641` n `18`; unknown avg `0.6466` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
