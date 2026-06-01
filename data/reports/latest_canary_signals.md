# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T16:37:30.442208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7095` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.8034` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2798` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1305` n `12`; crypto_alt avg `0.3628` n `228`; crypto_major avg `0.3445` n `8`; equity avg `-0.0054` n `69`; fx avg `0.0034` n `6`; index avg `-0.023` n `23`; metal avg `0.0791` n `18`; unknown avg `0.0165` n `422`
- 1h: commodity avg `0.5475` n `12`; crypto_alt avg `0.4711` n `228`; crypto_major avg `-0.1714` n `8`; equity avg `-0.3454` n `69`; fx avg `0.0466` n `6`; index avg `-0.0006` n `23`; metal avg `-0.3082` n `18`; unknown avg `-0.2022` n `422`
- 4h: commodity avg `1.3374` n `12`; crypto_alt avg `0.1686` n `228`; crypto_major avg `-1.3721` n `8`; equity avg `0.4313` n `69`; fx avg `-0.0134` n `6`; index avg `-0.0923` n `23`; metal avg `-0.4776` n `18`; unknown avg `0.5194` n `422`
- 24h: commodity avg `1.3938` n `12`; crypto_alt avg `1.1133` n `228`; crypto_major avg `-1.0276` n `8`; equity avg `-0.0859` n `69`; fx avg `0.0086` n `6`; index avg `0.2191` n `23`; metal avg `-0.2341` n `18`; unknown avg `3.6855` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2873`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.216`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
