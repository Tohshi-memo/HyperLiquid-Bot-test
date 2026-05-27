# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T23:52:19.698345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4887` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1276` n `12`; crypto_alt avg `0.2347` n `228`; crypto_major avg `0.1248` n `8`; equity avg `-0.1839` n `67`; fx avg `0.0056` n `6`; index avg `-0.0183` n `23`; metal avg `-0.1473` n `18`; unknown avg `0.0131` n `419`
- 1h: commodity avg `0.2857` n `12`; crypto_alt avg `-0.1513` n `228`; crypto_major avg `-0.4087` n `8`; equity avg `-0.3128` n `67`; fx avg `-0.0098` n `6`; index avg `-0.0984` n `23`; metal avg `-0.2233` n `18`; unknown avg `1.4309` n `419`
- 4h: commodity avg `0.2629` n `12`; crypto_alt avg `-2.0232` n `228`; crypto_major avg `-1.551` n `8`; equity avg `-0.436` n `67`; fx avg `-0.0207` n `6`; index avg `-0.0623` n `23`; metal avg `-0.1704` n `18`; unknown avg `0.081` n `419`
- 24h: commodity avg `-0.7963` n `12`; crypto_alt avg `-2.0773` n `228`; crypto_major avg `-1.5647` n `8`; equity avg `-0.7268` n `67`; fx avg `-0.1161` n `6`; index avg `-0.7134` n `23`; metal avg `-1.7964` n `18`; unknown avg `-0.6136` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
