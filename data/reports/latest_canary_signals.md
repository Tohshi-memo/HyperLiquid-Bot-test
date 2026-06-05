# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T17:37:21.394221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0141` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.1913` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0696` n `12`; crypto_alt avg `0.0442` n `228`; crypto_major avg `-0.1599` n `8`; equity avg `0.1738` n `74`; fx avg `-0.02` n `6`; index avg `0.0774` n `23`; metal avg `-0.0226` n `18`; unknown avg `-0.1285` n `424`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `0.9376` n `228`; crypto_major avg `0.3523` n `8`; equity avg `0.0653` n `74`; fx avg `-0.0242` n `6`; index avg `-0.2293` n `23`; metal avg `0.2105` n `18`; unknown avg `1.2773` n `424`
- 4h: commodity avg `-0.9249` n `12`; crypto_alt avg `-2.201` n `228`; crypto_major avg `-2.939` n `8`; equity avg `-2.9358` n `74`; fx avg `-0.1971` n `6`; index avg `-1.7477` n `23`; metal avg `-1.7637` n `18`; unknown avg `-0.3434` n `424`
- 24h: commodity avg `-1.3658` n `12`; crypto_alt avg `-7.5522` n `228`; crypto_major avg `-5.9976` n `8`; equity avg `-5.9483` n `74`; fx avg `-0.0579` n `6`; index avg `-3.4036` n `23`; metal avg `-4.0337` n `18`; unknown avg `-1.6554` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
