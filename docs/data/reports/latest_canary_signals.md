# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T12:22:26.220278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0489` n `12`; crypto_alt avg `0.0878` n `230`; crypto_major avg `0.1661` n `8`; equity avg `-0.002` n `92`; fx avg `0.0024` n `6`; index avg `-0.0038` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0073` n `765`
- 1h: commodity avg `-0.1118` n `12`; crypto_alt avg `0.3743` n `230`; crypto_major avg `0.3947` n `8`; equity avg `0.0243` n `92`; fx avg `0.0015` n `6`; index avg `0.007` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0113` n `765`
- 4h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `0.2829` n `8`; equity avg `0.0812` n `92`; fx avg `0.0006` n `6`; index avg `0.0027` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0399` n `763`
- 24h: commodity avg `0.3919` n `12`; crypto_alt avg `-0.7628` n `230`; crypto_major avg `-0.4104` n `8`; equity avg `-0.1076` n `92`; fx avg `0.0141` n `6`; index avg `-0.1163` n `25`; metal avg `-0.0991` n `20`; unknown avg `0.1092` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
