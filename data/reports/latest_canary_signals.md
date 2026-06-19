# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T17:07:29.577509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-5.5764` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-5.5764` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-5.1829` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-5.1829` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `5.1243` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `5.1243` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1018` n `12`; crypto_alt avg `-0.1565` n `228`; crypto_major avg `-0.182` n `8`; equity avg `-0.0638` n `78`; fx avg `0.0192` n `6`; index avg `-0.043` n `23`; metal avg `0.0051` n `18`; unknown avg `0.1752` n `687`
- 1h: commodity avg `0.2813` n `12`; crypto_alt avg `-3.6521` n `228`; crypto_major avg `-4.9016` n `8`; equity avg `0.6748` n `78`; fx avg `-0.0957` n `6`; index avg `0.2227` n `23`; metal avg `-4.2703` n `18`; unknown avg `-0.4432` n `572`
- 4h: commodity avg `0.2813` n `12`; crypto_alt avg `-3.6521` n `228`; crypto_major avg `-4.9016` n `8`; equity avg `0.6748` n `78`; fx avg `-0.0957` n `6`; index avg `0.2227` n `23`; metal avg `-4.2703` n `18`; unknown avg `-0.4432` n `572`
- 24h: commodity avg `0.2813` n `12`; crypto_alt avg `-3.6521` n `228`; crypto_major avg `-4.9016` n `8`; equity avg `0.6748` n `78`; fx avg `-0.0957` n `6`; index avg `0.2227` n `23`; metal avg `-4.2703` n `18`; unknown avg `-0.4432` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
