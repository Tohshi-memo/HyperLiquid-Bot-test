# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T13:52:27.691769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.3214` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.2213` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2816` n `12`; crypto_alt avg `-0.5221` n `228`; crypto_major avg `-0.5571` n `8`; equity avg `0.1839` n `69`; fx avg `-0.049` n `6`; index avg `0.1975` n `23`; metal avg `-0.239` n `18`; unknown avg `-0.0359` n `422`
- 1h: commodity avg `1.1784` n `12`; crypto_alt avg `-0.7129` n `228`; crypto_major avg `-1.143` n `8`; equity avg `-0.3725` n `69`; fx avg `-0.0972` n `6`; index avg `-0.1498` n `23`; metal avg `-1.1705` n `18`; unknown avg `0.7777` n `422`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `-0.8395` n `228`; crypto_major avg `-1.3938` n `8`; equity avg `-0.5384` n `69`; fx avg `-0.1002` n `6`; index avg `-0.1725` n `23`; metal avg `-0.8316` n `18`; unknown avg `3.6371` n `416`
- 24h: commodity avg `1.114` n `12`; crypto_alt avg `-1.2707` n `228`; crypto_major avg `-1.8609` n `8`; equity avg `-0.8737` n `69`; fx avg `-0.0923` n `6`; index avg `0.3061` n `23`; metal avg `-0.7665` n `18`; unknown avg `4.381` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2844`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
