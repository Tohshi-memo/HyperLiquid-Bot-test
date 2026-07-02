# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T11:52:34.842097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5654` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1206` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.0044` n `229`; crypto_major avg `0.1069` n `8`; equity avg `0.2174` n `88`; fx avg `-0.0169` n `6`; index avg `0.0669` n `25`; metal avg `0.0776` n `20`; unknown avg `-0.1297` n `763`
- 1h: commodity avg `-0.1288` n `12`; crypto_alt avg `0.1769` n `229`; crypto_major avg `0.4492` n `8`; equity avg `0.3886` n `88`; fx avg `-0.0287` n `6`; index avg `0.0829` n `25`; metal avg `0.1101` n `20`; unknown avg `-0.2338` n `763`
- 4h: commodity avg `-0.2322` n `12`; crypto_alt avg `1.2977` n `228`; crypto_major avg `2.3332` n `8`; equity avg `0.8729` n `88`; fx avg `-0.0352` n `6`; index avg `0.1062` n `25`; metal avg `0.2126` n `20`; unknown avg `0.4645` n `763`
- 24h: commodity avg `-0.6006` n `12`; crypto_alt avg `3.1706` n `228`; crypto_major avg `4.4971` n `8`; equity avg `-1.5602` n `88`; fx avg `-0.1313` n `6`; index avg `-0.4925` n `25`; metal avg `0.6903` n `20`; unknown avg `2.3886` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
