# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T15:22:31.525497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4417` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1069` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5325` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0059` n `13`; crypto_alt avg `-0.1036` n `239`; crypto_major avg `-0.0216` n `8`; equity avg `0.359` n `162`; fx avg `-0.0231` n `6`; index avg `0.0315` n `27`; metal avg `-0.048` n `20`; unknown avg `1.4124` n `1259`
- 1h: commodity avg `0.0967` n `13`; crypto_alt avg `-0.0691` n `239`; crypto_major avg `0.1569` n `8`; equity avg `0.9297` n `162`; fx avg `-0.0384` n `6`; index avg `0.1063` n `27`; metal avg `-0.337` n `20`; unknown avg `1.8656` n `1253`
- 4h: commodity avg `0.3256` n `13`; crypto_alt avg `-1.8636` n `239`; crypto_major avg `-2.1161` n `8`; equity avg `-1.2437` n `162`; fx avg `-0.0299` n `6`; index avg `-0.0092` n `27`; metal avg `-0.5836` n `20`; unknown avg `21.4412` n `1239`
- 24h: commodity avg `-0.2663` n `13`; crypto_alt avg `-3.7314` n `239`; crypto_major avg `-3.0309` n `8`; equity avg `-2.6024` n `162`; fx avg `-0.1212` n `6`; index avg `-0.0835` n `27`; metal avg `-1.1674` n `20`; unknown avg `5.724` n `1148`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
