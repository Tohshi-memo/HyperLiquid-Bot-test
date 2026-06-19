# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T17:28:54.060586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.553` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-5.1188` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `5.0853` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `0.0503` n `228`; crypto_major avg `0.0477` n `8`; equity avg `0.02` n `78`; fx avg `0.0023` n `6`; index avg `0.0052` n `23`; metal avg `0.0155` n `18`; unknown avg `-0.0502` n `687`
- 1h: commodity avg `-0.1774` n `12`; crypto_alt avg `-0.4385` n `228`; crypto_major avg `-0.517` n `8`; equity avg `-0.1683` n `78`; fx avg `0.0155` n `6`; index avg `-0.0384` n `23`; metal avg `0.1782` n `18`; unknown avg `0.0757` n `687`
- 4h: commodity avg `0.2617` n `12`; crypto_alt avg `-3.6075` n `228`; crypto_major avg `-4.8571` n `8`; equity avg `0.6959` n `78`; fx avg `-0.0935` n `6`; index avg `0.2282` n `23`; metal avg `-4.2559` n `18`; unknown avg `-0.3972` n `572`
- 24h: commodity avg `0.2617` n `12`; crypto_alt avg `-3.6075` n `228`; crypto_major avg `-4.8571` n `8`; equity avg `0.6959` n `78`; fx avg `-0.0935` n `6`; index avg `0.2282` n `23`; metal avg `-4.2559` n `18`; unknown avg `-0.3972` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
