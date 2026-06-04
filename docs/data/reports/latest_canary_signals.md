# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T12:37:24.063253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.2795` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.7353` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `1.6742` n `228`; crypto_major avg `1.404` n `8`; equity avg `0.6059` n `73`; fx avg `0.0052` n `6`; index avg `0.0797` n `23`; metal avg `0.0458` n `18`; unknown avg `0.9694` n `423`
- 1h: commodity avg `-0.0727` n `12`; crypto_alt avg `2.3984` n `228`; crypto_major avg `2.2068` n `8`; equity avg `0.8493` n `73`; fx avg `0.0112` n `6`; index avg `0.1359` n `23`; metal avg `0.4715` n `18`; unknown avg `1.327` n `422`
- 4h: commodity avg `-0.352` n `12`; crypto_alt avg `0.2423` n `228`; crypto_major avg `0.4275` n `8`; equity avg `-0.1915` n `73`; fx avg `0.0289` n `6`; index avg `-0.2789` n `23`; metal avg `0.8197` n `18`; unknown avg `-0.3107` n `422`
- 24h: commodity avg `-0.9905` n `12`; crypto_alt avg `-6.2915` n `228`; crypto_major avg `-4.8853` n `8`; equity avg `-3.9155` n `73`; fx avg `0.0866` n `6`; index avg `-1.4526` n `23`; metal avg `0.1978` n `18`; unknown avg `-1.0668` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
