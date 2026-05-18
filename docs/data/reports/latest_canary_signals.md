# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T16:52:16.571915+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6302` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0164` n `228`; crypto_major avg `0.0878` n `8`; equity avg `0.2618` n `66`; fx avg `-0.0081` n `5`; index avg `0.0439` n `23`; metal avg `0.1171` n `18`; unknown avg `-0.1591` n `384`
- 1h: commodity avg `0.1758` n `12`; crypto_alt avg `0.1507` n `228`; crypto_major avg `0.2324` n `8`; equity avg `-0.0239` n `66`; fx avg `0.0024` n `5`; index avg `-0.0116` n `23`; metal avg `0.2327` n `18`; unknown avg `-0.1409` n `384`
- 4h: commodity avg `1.3114` n `12`; crypto_alt avg `-1.0309` n `228`; crypto_major avg `-1.3188` n `8`; equity avg `-2.1945` n `66`; fx avg `0.0087` n `5`; index avg `-0.9529` n `23`; metal avg `-0.1475` n `18`; unknown avg `0.4308` n `383`
- 24h: commodity avg `1.0612` n `12`; crypto_alt avg `-2.5029` n `228`; crypto_major avg `-1.8826` n `8`; equity avg `-0.9344` n `66`; fx avg `0.057` n `5`; index avg `-0.4173` n `23`; metal avg `0.5731` n `18`; unknown avg `-0.2837` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
