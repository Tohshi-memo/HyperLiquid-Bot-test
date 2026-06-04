# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T09:22:26.176797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.3649` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.2725` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.949` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1197` n `12`; crypto_alt avg `-0.7399` n `228`; crypto_major avg `-0.5582` n `8`; equity avg `-0.4094` n `73`; fx avg `0.0155` n `6`; index avg `-0.0888` n `23`; metal avg `0.0063` n `18`; unknown avg `-0.2614` n `424`
- 1h: commodity avg `-0.1398` n `12`; crypto_alt avg `-0.9017` n `228`; crypto_major avg `-0.6627` n `8`; equity avg `-0.8261` n `73`; fx avg `-0.0058` n `6`; index avg `-0.226` n `23`; metal avg `0.1236` n `18`; unknown avg `-0.7039` n `424`
- 4h: commodity avg `-0.1258` n `12`; crypto_alt avg `-2.2056` n `228`; crypto_major avg `-2.3983` n `8`; equity avg `-1.2826` n `73`; fx avg `0.1171` n `6`; index avg `-0.4493` n `23`; metal avg `-0.0334` n `18`; unknown avg `-0.3493` n `404`
- 24h: commodity avg `-0.8822` n `12`; crypto_alt avg `-6.9823` n `228`; crypto_major avg `-6.1859` n `8`; equity avg `-4.788` n `73`; fx avg `0.082` n `6`; index avg `-1.5475` n `23`; metal avg `-1.0439` n `18`; unknown avg `-1.3542` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
