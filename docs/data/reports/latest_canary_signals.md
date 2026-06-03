# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T01:52:20.667709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2086` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0033` n `228`; crypto_major avg `0.142` n `8`; equity avg `-0.1158` n `69`; fx avg `0.0038` n `6`; index avg `-0.061` n `23`; metal avg `0.1135` n `18`; unknown avg `0.002` n `422`
- 1h: commodity avg `0.1177` n `12`; crypto_alt avg `-0.2453` n `228`; crypto_major avg `-0.5497` n `8`; equity avg `-0.3387` n `69`; fx avg `-0.0176` n `6`; index avg `-0.0773` n `23`; metal avg `-0.4311` n `18`; unknown avg `-0.4665` n `422`
- 4h: commodity avg `0.492` n `12`; crypto_alt avg `-1.0737` n `228`; crypto_major avg `-1.0836` n `8`; equity avg `-0.4157` n `69`; fx avg `0.0022` n `6`; index avg `0.125` n `23`; metal avg `-0.3643` n `18`; unknown avg `-0.9842` n `422`
- 24h: commodity avg `0.6355` n `12`; crypto_alt avg `-3.5683` n `228`; crypto_major avg `-5.3551` n `8`; equity avg `1.7531` n `69`; fx avg `0.0176` n `6`; index avg `1.5125` n `23`; metal avg `0.3747` n `18`; unknown avg `-1.1465` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
