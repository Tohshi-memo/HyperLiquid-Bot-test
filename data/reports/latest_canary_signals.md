# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T16:37:32.574765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-5.2387` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-5.2387` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-4.7692` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-4.7692` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `4.6696` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `4.6696` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.065` n `12`; crypto_alt avg `0.0041` n `228`; crypto_major avg `-0.0313` n `8`; equity avg `-0.025` n `78`; fx avg `-0.0128` n `6`; index avg `0.0066` n `23`; metal avg `0.026` n `18`; unknown avg `0.0455` n `687`
- 1h: commodity avg `0.3752` n `12`; crypto_alt avg `-3.1891` n `228`; crypto_major avg `-4.394` n `8`; equity avg `0.8447` n `78`; fx avg `-0.1217` n `6`; index avg `0.2756` n `23`; metal avg `-4.3974` n `18`; unknown avg `-0.3932` n `572`
- 4h: commodity avg `0.3752` n `12`; crypto_alt avg `-3.1891` n `228`; crypto_major avg `-4.394` n `8`; equity avg `0.8447` n `78`; fx avg `-0.1217` n `6`; index avg `0.2756` n `23`; metal avg `-4.3974` n `18`; unknown avg `-0.3932` n `572`
- 24h: commodity avg `0.3752` n `12`; crypto_alt avg `-3.1891` n `228`; crypto_major avg `-4.394` n `8`; equity avg `0.8447` n `78`; fx avg `-0.1217` n `6`; index avg `0.2756` n `23`; metal avg `-4.3974` n `18`; unknown avg `-0.3932` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0718`, n `670`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0678`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `670`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0624`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0597`, n `670`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `670`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0508`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0497`, n `670`, weak_sample_signal
