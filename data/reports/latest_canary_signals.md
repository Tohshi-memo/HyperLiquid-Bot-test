# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T12:22:23.717222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.75` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `0.017` n `228`; crypto_major avg `-0.0586` n `8`; equity avg `0.1283` n `69`; fx avg `0.0001` n `6`; index avg `0.0418` n `23`; metal avg `0.1194` n `18`; unknown avg `-0.0219` n `422`
- 1h: commodity avg `-0.1461` n `12`; crypto_alt avg `-0.0886` n `228`; crypto_major avg `-0.0414` n `8`; equity avg `0.1499` n `69`; fx avg `0.0001` n `6`; index avg `0.1025` n `23`; metal avg `0.1184` n `18`; unknown avg `-0.1793` n `422`
- 4h: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.0179` n `228`; crypto_major avg `-0.2371` n `8`; equity avg `0.0061` n `69`; fx avg `0.0055` n `6`; index avg `0.0579` n `23`; metal avg `-0.3231` n `18`; unknown avg `-0.1882` n `422`
- 24h: commodity avg `-0.4131` n `12`; crypto_alt avg `0.1441` n `228`; crypto_major avg `-1.7889` n `8`; equity avg `1.0052` n `69`; fx avg `0.1373` n `6`; index avg `0.2341` n `23`; metal avg `0.992` n `18`; unknown avg `0.1283` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
