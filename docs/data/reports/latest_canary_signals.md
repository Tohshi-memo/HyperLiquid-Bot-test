# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T17:22:30.386021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2346` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.0641` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.209` n `12`; crypto_alt avg `0.4437` n `228`; crypto_major avg `0.304` n `8`; equity avg `0.0523` n `73`; fx avg `0.0016` n `6`; index avg `-0.0264` n `23`; metal avg `-0.0766` n `18`; unknown avg `0.966` n `419`
- 1h: commodity avg `0.1281` n `12`; crypto_alt avg `0.4056` n `228`; crypto_major avg `0.3827` n `8`; equity avg `-0.2582` n `73`; fx avg `-0.0114` n `6`; index avg `-0.0624` n `23`; metal avg `0.0171` n `18`; unknown avg `-0.0545` n `419`
- 4h: commodity avg `0.5338` n `12`; crypto_alt avg `-1.264` n `228`; crypto_major avg `-1.7008` n `8`; equity avg `-2.3685` n `73`; fx avg `0.0026` n `6`; index avg `-0.6367` n `23`; metal avg `-0.837` n `18`; unknown avg `0.867` n `419`
- 24h: commodity avg `0.9463` n `12`; crypto_alt avg `-0.1953` n `228`; crypto_major avg `-3.0433` n `8`; equity avg `-2.3292` n `72`; fx avg `0.0256` n `6`; index avg `-0.2698` n `23`; metal avg `-1.8534` n `18`; unknown avg `0.8827` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
