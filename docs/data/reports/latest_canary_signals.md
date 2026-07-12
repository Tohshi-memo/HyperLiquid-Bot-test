# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T19:57:09.537632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0643` n `12`; crypto_alt avg `0.1266` n `230`; crypto_major avg `0.1794` n `8`; equity avg `0.0104` n `92`; fx avg `0.0031` n `6`; index avg `0.0008` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0957` n `765`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `0.1748` n `230`; crypto_major avg `0.0728` n `8`; equity avg `0.0745` n `92`; fx avg `0.0088` n `6`; index avg `0.0186` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.102` n `765`
- 4h: commodity avg `0.1465` n `12`; crypto_alt avg `-0.0427` n `230`; crypto_major avg `0.0787` n `8`; equity avg `0.05` n `92`; fx avg `-0.0146` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.2196` n `759`
- 24h: commodity avg `0.6066` n `12`; crypto_alt avg `-1.2666` n `230`; crypto_major avg `-0.4` n `8`; equity avg `-0.1701` n `92`; fx avg `0.0053` n `6`; index avg `-0.093` n `25`; metal avg `-0.1016` n `20`; unknown avg `0.1764` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
