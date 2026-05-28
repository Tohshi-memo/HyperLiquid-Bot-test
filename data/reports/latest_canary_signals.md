# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T01:07:21.358228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.271` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0807` n `12`; crypto_alt avg `0.0544` n `228`; crypto_major avg `0.0299` n `8`; equity avg `0.0614` n `67`; fx avg `0.0013` n `6`; index avg `0.0348` n `23`; metal avg `-0.2473` n `18`; unknown avg `0.118` n `419`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.1241` n `228`; crypto_major avg `0.109` n `8`; equity avg `0.2638` n `67`; fx avg `-0.0126` n `6`; index avg `0.1786` n `23`; metal avg `-0.0907` n `18`; unknown avg `0.1591` n `419`
- 4h: commodity avg `0.3119` n `12`; crypto_alt avg `-1.9071` n `228`; crypto_major avg `-1.4197` n `8`; equity avg `-0.2598` n `67`; fx avg `-0.0162` n `6`; index avg `-0.1487` n `23`; metal avg `-0.2189` n `18`; unknown avg `0.4051` n `419`
- 24h: commodity avg `-0.7029` n `12`; crypto_alt avg `-2.5464` n `228`; crypto_major avg `-1.8515` n `8`; equity avg `-0.5454` n `67`; fx avg `-0.074` n `6`; index avg `-0.6945` n `23`; metal avg `-1.6078` n `18`; unknown avg `-0.8898` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
