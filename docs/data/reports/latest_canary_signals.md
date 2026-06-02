# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T19:34:45.224492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.01` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.4401` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-1.3052` n `228`; crypto_major avg `-0.9727` n `8`; equity avg `-0.131` n `69`; fx avg `0.0029` n `6`; index avg `-0.057` n `23`; metal avg `0.0035` n `18`; unknown avg `-0.5285` n `422`
- 1h: commodity avg `-0.1071` n `12`; crypto_alt avg `-1.8889` n `228`; crypto_major avg `-1.3905` n `8`; equity avg `-0.0403` n `69`; fx avg `0.0321` n `6`; index avg `0.0496` n `23`; metal avg `-0.0206` n `18`; unknown avg `-1.0942` n `422`
- 4h: commodity avg `0.5213` n `12`; crypto_alt avg `-0.436` n `228`; crypto_major avg `-0.9953` n `8`; equity avg `-0.0544` n `69`; fx avg `-0.0088` n `6`; index avg `-0.0651` n `23`; metal avg `-0.6134` n `18`; unknown avg `0.0998` n `422`
- 24h: commodity avg `-0.0167` n `12`; crypto_alt avg `-5.6378` n `228`; crypto_major avg `-5.7533` n `8`; equity avg `0.3287` n `69`; fx avg `0.0865` n `6`; index avg `0.2304` n `23`; metal avg `0.2513` n `18`; unknown avg `-0.7779` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
