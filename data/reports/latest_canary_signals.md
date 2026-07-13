# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T03:07:26.132049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0367` n `12`; crypto_alt avg `-0.7241` n `230`; crypto_major avg `-0.6168` n `8`; equity avg `-0.526` n `92`; fx avg `0.024` n `6`; index avg `-0.0936` n `25`; metal avg `-0.163` n `20`; unknown avg `0.229` n `766`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.3257` n `230`; crypto_major avg `-0.25` n `8`; equity avg `-0.1539` n `92`; fx avg `0.0203` n `6`; index avg `0.0049` n `25`; metal avg `-0.151` n `20`; unknown avg `-0.1046` n `766`
- 4h: commodity avg `0.105` n `12`; crypto_alt avg `-0.9241` n `230`; crypto_major avg `-0.758` n `8`; equity avg `-1.7491` n `92`; fx avg `0.106` n `6`; index avg `-0.3668` n `25`; metal avg `-0.1671` n `20`; unknown avg `0.2685` n `766`
- 24h: commodity avg `0.0738` n `12`; crypto_alt avg `-1.8394` n `230`; crypto_major avg `-0.9312` n `8`; equity avg `-2.0768` n `92`; fx avg `0.0356` n `6`; index avg `-0.4202` n `25`; metal avg `-0.4801` n `20`; unknown avg `-0.0672` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1822`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.18`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1133`, n `670`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1125`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `670`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0891`, n `670`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `670`, weak_sample_signal
