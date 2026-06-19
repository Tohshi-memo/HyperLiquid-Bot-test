# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T19:22:30.688082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2582` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8649` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.8008` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.1948` n `228`; crypto_major avg `-0.0342` n `8`; equity avg `0.0086` n `78`; fx avg `-0.0221` n `6`; index avg `0.0062` n `23`; metal avg `0.0133` n `18`; unknown avg `-0.1687` n `687`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `-0.5259` n `228`; crypto_major avg `-0.1532` n `8`; equity avg `-0.0283` n `78`; fx avg `-0.0082` n `6`; index avg `0.003` n `23`; metal avg `0.0403` n `18`; unknown avg `-0.0706` n `687`
- 4h: commodity avg `0.296` n `12`; crypto_alt avg `-3.8627` n `228`; crypto_major avg `-4.5689` n `8`; equity avg `0.6893` n `78`; fx avg `-0.0985` n `6`; index avg `0.2319` n `23`; metal avg `-4.2324` n `18`; unknown avg `-0.4474` n `572`
- 24h: commodity avg `0.296` n `12`; crypto_alt avg `-3.8627` n `228`; crypto_major avg `-4.5689` n `8`; equity avg `0.6893` n `78`; fx avg `-0.0985` n `6`; index avg `0.2319` n `23`; metal avg `-4.2324` n `18`; unknown avg `-0.4474` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
