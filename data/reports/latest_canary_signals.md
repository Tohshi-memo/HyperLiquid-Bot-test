# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T02:22:12.588834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5806` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.5209` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3017` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1022` n `12`; crypto_alt avg `-0.0606` n `228`; crypto_major avg `-0.1583` n `8`; equity avg `0.3257` n `66`; fx avg `0.0146` n `5`; index avg `0.1278` n `23`; metal avg `0.2502` n `18`; unknown avg `0.1485` n `383`
- 1h: commodity avg `-0.2807` n `12`; crypto_alt avg `0.3808` n `228`; crypto_major avg `0.122` n `8`; equity avg `0.7653` n `66`; fx avg `0.0659` n `5`; index avg `0.2279` n `23`; metal avg `0.5451` n `18`; unknown avg `-0.3407` n `383`
- 4h: commodity avg `0.9649` n `12`; crypto_alt avg `-1.555` n `228`; crypto_major avg `-1.6157` n `8`; equity avg `-0.0948` n `66`; fx avg `0.1182` n `5`; index avg `-0.314` n `23`; metal avg `-0.7167` n `18`; unknown avg `0.2439` n `383`
- 24h: commodity avg `2.6912` n `12`; crypto_alt avg `-10.832` n `228`; crypto_major avg `-3.1798` n `8`; equity avg `-2.9554` n `65`; fx avg `-0.054` n `5`; index avg `-1.7639` n `23`; metal avg `-6.2818` n `18`; unknown avg `550.2425` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
