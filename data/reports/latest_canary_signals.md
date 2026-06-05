# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T06:22:22.726987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8301` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.7361` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.3135` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.1949` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-3.1817` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `3.163` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.8146` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.5802` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `-2.353` n `228`; crypto_major avg `-1.8638` n `8`; equity avg `-0.4577` n `74`; fx avg `0.0331` n `6`; index avg `-0.107` n `23`; metal avg `-0.2608` n `18`; unknown avg `-0.6781` n `424`
- 1h: commodity avg `-0.1069` n `12`; crypto_alt avg `-3.9821` n `228`; crypto_major avg `-3.3018` n `8`; equity avg `-0.7216` n `74`; fx avg `0.0279` n `6`; index avg `-0.1388` n `23`; metal avg `-0.4872` n `18`; unknown avg `-1.0854` n `404`
- 4h: commodity avg `-0.1322` n `12`; crypto_alt avg `-4.4311` n `228`; crypto_major avg `-3.9623` n `8`; equity avg `-0.7806` n `74`; fx avg `-0.0118` n `6`; index avg `-0.2262` n `23`; metal avg `-0.6488` n `18`; unknown avg `-1.2358` n `404`
- 24h: commodity avg `-0.2892` n `12`; crypto_alt avg `-8.658` n `228`; crypto_major avg `-7.538` n `8`; equity avg `-1.9638` n `73`; fx avg `0.1909` n `6`; index avg `-0.5597` n `23`; metal avg `-0.8869` n `18`; unknown avg `-2.3522` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
