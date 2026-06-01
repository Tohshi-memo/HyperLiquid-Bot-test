# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T15:07:56.452711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0851` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2816` n `12`; crypto_alt avg `0.4063` n `228`; crypto_major avg `0.2978` n `8`; equity avg `0.3749` n `69`; fx avg `0.0242` n `6`; index avg `0.1148` n `23`; metal avg `0.2663` n `18`; unknown avg `0.272` n `422`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `0.3259` n `228`; crypto_major avg `-0.0146` n `8`; equity avg `0.4817` n `69`; fx avg `0.033` n `6`; index avg `0.0126` n `23`; metal avg `0.3526` n `18`; unknown avg `0.0604` n `422`
- 4h: commodity avg `0.32` n `12`; crypto_alt avg `-0.6038` n `228`; crypto_major avg `-1.3595` n `8`; equity avg `-0.125` n `69`; fx avg `-0.0447` n `6`; index avg `-0.2744` n `23`; metal avg `-0.6276` n `18`; unknown avg `1.8906` n `416`
- 24h: commodity avg `1.1749` n `12`; crypto_alt avg `0.0476` n `228`; crypto_major avg `-1.5151` n `8`; equity avg `-0.3225` n `69`; fx avg `-0.0485` n `6`; index avg `0.2814` n `23`; metal avg `-0.4192` n `18`; unknown avg `3.5551` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2835`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
