# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T08:22:25.039432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7155` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.413` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.3549` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.892` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0453` n `12`; crypto_alt avg `-0.5098` n `228`; crypto_major avg `-0.5039` n `8`; equity avg `-0.4406` n `73`; fx avg `0.0046` n `6`; index avg `-0.2259` n `23`; metal avg `-0.0769` n `18`; unknown avg `1.0954` n `424`
- 1h: commodity avg `0.1435` n `12`; crypto_alt avg `-0.8624` n `228`; crypto_major avg `-0.7295` n `8`; equity avg `-0.4588` n `73`; fx avg `0.047` n `6`; index avg `-0.2494` n `23`; metal avg `0.055` n `18`; unknown avg `-0.0492` n `424`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `-3.5801` n `228`; crypto_major avg `-3.649` n `8`; equity avg `-0.757` n `73`; fx avg `0.1177` n `6`; index avg `-0.236` n `23`; metal avg `-0.2941` n `18`; unknown avg `0.1032` n `404`
- 24h: commodity avg `-0.643` n `12`; crypto_alt avg `-6.4017` n `228`; crypto_major avg `-5.6058` n `8`; equity avg `-4.1479` n `73`; fx avg `0.0877` n `6`; index avg `-1.325` n `23`; metal avg `-1.0016` n `18`; unknown avg `-0.6628` n `403`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
