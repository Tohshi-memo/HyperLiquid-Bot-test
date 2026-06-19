# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T19:07:33.964110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2201` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8291` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.7639` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.1135` n `228`; crypto_major avg `0.0203` n `8`; equity avg `-0.005` n `78`; fx avg `0.021` n `6`; index avg `0.0159` n `23`; metal avg `-0.0004` n `18`; unknown avg `-0.0653` n `687`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.3839` n `228`; crypto_major avg `-0.0448` n `8`; equity avg `-0.0369` n `78`; fx avg `0.0281` n `6`; index avg `-0.0017` n `23`; metal avg `0.0052` n `18`; unknown avg `0.0578` n `687`
- 4h: commodity avg `0.291` n `12`; crypto_alt avg `-3.6789` n `228`; crypto_major avg `-4.5381` n `8`; equity avg `0.682` n `78`; fx avg `-0.0764` n `6`; index avg `0.2258` n `23`; metal avg `-4.2447` n `18`; unknown avg `-0.263` n `572`
- 24h: commodity avg `0.291` n `12`; crypto_alt avg `-3.6789` n `228`; crypto_major avg `-4.5381` n `8`; equity avg `0.682` n `78`; fx avg `-0.0764` n `6`; index avg `0.2258` n `23`; metal avg `-4.2447` n `18`; unknown avg `-0.263` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
