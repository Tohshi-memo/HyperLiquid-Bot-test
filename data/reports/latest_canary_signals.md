# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T03:37:33.457408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.1567` n `230`; crypto_major avg `0.062` n `8`; equity avg `0.0029` n `92`; fx avg `0.0038` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0208` n `765`
- 1h: commodity avg `-0.1539` n `12`; crypto_alt avg `0.3339` n `230`; crypto_major avg `0.0734` n `8`; equity avg `0.0204` n `92`; fx avg `0.0031` n `6`; index avg `-0.019` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.1575` n `765`
- 4h: commodity avg `0.0255` n `12`; crypto_alt avg `0.5909` n `230`; crypto_major avg `0.1651` n `8`; equity avg `0.0748` n `92`; fx avg `-0.0078` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0244` n `20`; unknown avg `-0.1144` n `765`
- 24h: commodity avg `0.368` n `12`; crypto_alt avg `-0.4841` n `229`; crypto_major avg `-0.3594` n `8`; equity avg `0.0671` n `92`; fx avg `0.0205` n `6`; index avg `-0.1204` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.0977` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
