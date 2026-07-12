# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T02:22:29.814597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0259` n `230`; crypto_major avg `0.0728` n `8`; equity avg `-0.0091` n `92`; fx avg `-0.0017` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0571` n `765`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `0.2543` n `230`; crypto_major avg `0.2177` n `8`; equity avg `0.0414` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.1747` n `765`
- 4h: commodity avg `0.1061` n `12`; crypto_alt avg `-0.6927` n `230`; crypto_major avg `-0.7999` n `8`; equity avg `-0.2018` n `92`; fx avg `0.0084` n `6`; index avg `-0.135` n `25`; metal avg `-0.0418` n `20`; unknown avg `0.2052` n `765`
- 24h: commodity avg `0.5595` n `12`; crypto_alt avg `-0.525` n `229`; crypto_major avg `-0.1696` n `8`; equity avg `0.0646` n `92`; fx avg `0.0231` n `6`; index avg `-0.0867` n `25`; metal avg `-0.0719` n `20`; unknown avg `-0.169` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
