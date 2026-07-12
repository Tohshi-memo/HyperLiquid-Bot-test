# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T19:37:27.129790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0353` n `230`; crypto_major avg `-0.1035` n `8`; equity avg `0.0086` n `92`; fx avg `-0.0075` n `6`; index avg `0.0044` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0392` n `765`
- 1h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.0506` n `230`; crypto_major avg `-0.0643` n `8`; equity avg `0.0554` n `92`; fx avg `0.005` n `6`; index avg `0.0302` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0258` n `765`
- 4h: commodity avg `0.1139` n `12`; crypto_alt avg `-0.1199` n `230`; crypto_major avg `0.0135` n `8`; equity avg `0.0513` n `92`; fx avg `-0.0186` n `6`; index avg `0.016` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.1534` n `759`
- 24h: commodity avg `0.5379` n `12`; crypto_alt avg `-1.3548` n `230`; crypto_major avg `-0.5667` n `8`; equity avg `-0.1695` n `92`; fx avg `0.0038` n `6`; index avg `-0.0915` n `25`; metal avg `-0.1056` n `20`; unknown avg `0.1651` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
