# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T14:37:46.381236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0664` n `230`; crypto_major avg `0.1148` n `8`; equity avg `0.0105` n `92`; fx avg `0.0` n `6`; index avg `-0.0001` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0005` n `765`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `-0.1922` n `230`; crypto_major avg `-0.0582` n `8`; equity avg `-0.0046` n `92`; fx avg `0.0069` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.0043` n `765`
- 4h: commodity avg `-0.0463` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.5108` n `8`; equity avg `0.0933` n `92`; fx avg `0.0054` n `6`; index avg `0.0171` n `25`; metal avg `-0.0178` n `20`; unknown avg `-0.1831` n `763`
- 24h: commodity avg `0.4708` n `12`; crypto_alt avg `-1.4897` n `230`; crypto_major avg `-0.9092` n `8`; equity avg `-0.0686` n `92`; fx avg `0.0221` n `6`; index avg `-0.1066` n `25`; metal avg `-0.1189` n `20`; unknown avg `0.0974` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
