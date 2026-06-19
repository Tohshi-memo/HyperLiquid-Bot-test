# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T19:17:23.926857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.2498` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-4.8536` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.7812` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.1107` n `228`; crypto_major avg `-0.0124` n `8`; equity avg `0.0197` n `78`; fx avg `-0.0169` n `6`; index avg `0.0065` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.1255` n `687`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `-0.4421` n `228`; crypto_major avg `-0.1316` n `8`; equity avg `-0.0172` n `78`; fx avg `-0.0029` n `6`; index avg `0.0034` n `23`; metal avg `0.0297` n `18`; unknown avg `-0.0397` n `687`
- 4h: commodity avg `0.3047` n `12`; crypto_alt avg `-3.7837` n `228`; crypto_major avg `-4.5489` n `8`; equity avg `0.7009` n `78`; fx avg `-0.0934` n `6`; index avg `0.2323` n `23`; metal avg `-4.2423` n `18`; unknown avg `-0.3999` n `572`
- 24h: commodity avg `0.3047` n `12`; crypto_alt avg `-3.7837` n `228`; crypto_major avg `-4.5489` n `8`; equity avg `0.7009` n `78`; fx avg `-0.0934` n `6`; index avg `0.2323` n `23`; metal avg `-4.2423` n `18`; unknown avg `-0.3999` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
