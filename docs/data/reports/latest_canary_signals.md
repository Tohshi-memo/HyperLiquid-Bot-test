# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T18:52:28.821762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.244` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8607` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.767` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `0.0289` n `8`; equity avg `-0.0101` n `78`; fx avg `-0.026` n `6`; index avg `-0.0118` n `23`; metal avg `-0.0008` n `18`; unknown avg `0.0994` n `687`
- 1h: commodity avg `0.0514` n `12`; crypto_alt avg `-0.3423` n `228`; crypto_major avg `-0.1017` n `8`; equity avg `-0.0401` n `78`; fx avg `-0.0305` n `6`; index avg `-0.0049` n `23`; metal avg `0.0058` n `18`; unknown avg `0.0627` n `687`
- 4h: commodity avg `0.3029` n `12`; crypto_alt avg `-3.5668` n `228`; crypto_major avg `-4.5578` n `8`; equity avg `0.6862` n `78`; fx avg `-0.0978` n `6`; index avg `0.2092` n `23`; metal avg `-4.2442` n `18`; unknown avg `-0.2168` n `572`
- 24h: commodity avg `0.3029` n `12`; crypto_alt avg `-3.5668` n `228`; crypto_major avg `-4.5578` n `8`; equity avg `0.6862` n `78`; fx avg `-0.0978` n `6`; index avg `0.2092` n `23`; metal avg `-4.2442` n `18`; unknown avg `-0.2168` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
