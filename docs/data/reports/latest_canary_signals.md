# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T17:22:33.298000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.4414` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.9249` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.9136` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.2033` n `228`; crypto_major avg `0.2307` n `8`; equity avg `0.0811` n `78`; fx avg `0.0173` n `6`; index avg `0.0064` n `23`; metal avg `0.017` n `18`; unknown avg `-0.0865` n `687`
- 1h: commodity avg `-0.1981` n `12`; crypto_alt avg `-0.2864` n `228`; crypto_major avg `-0.3354` n `8`; equity avg `-0.1075` n `78`; fx avg `0.0305` n `6`; index avg `-0.0372` n `23`; metal avg `0.1796` n `18`; unknown avg `-0.0072` n `687`
- 4h: commodity avg `0.2407` n `12`; crypto_alt avg `-3.4621` n `228`; crypto_major avg `-4.6842` n `8`; equity avg `0.7572` n `78`; fx avg `-0.0783` n `6`; index avg `0.2294` n `23`; metal avg `-4.2545` n `18`; unknown avg `-0.3899` n `572`
- 24h: commodity avg `0.2407` n `12`; crypto_alt avg `-3.4621` n `228`; crypto_major avg `-4.6842` n `8`; equity avg `0.7572` n `78`; fx avg `-0.0783` n `6`; index avg `0.2294` n `23`; metal avg `-4.2545` n `18`; unknown avg `-0.3899` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
