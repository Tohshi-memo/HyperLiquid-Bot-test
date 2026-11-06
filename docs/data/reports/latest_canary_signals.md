# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T20:51:06.707542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.059` n `239`; crypto_major avg `-0.0774` n `8`; equity avg `-0.2053` n `158`; fx avg `0.0024` n `6`; index avg `-0.0371` n `27`; metal avg `-0.0245` n `20`; unknown avg `134.3678` n `1261`
- 1h: commodity avg `-0.1005` n `13`; crypto_alt avg `-0.0593` n `239`; crypto_major avg `-0.1121` n `8`; equity avg `0.0319` n `158`; fx avg `0.0023` n `6`; index avg `-0.0345` n `27`; metal avg `0.0263` n `20`; unknown avg `107.6569` n `1235`
- 4h: commodity avg `0.1652` n `13`; crypto_alt avg `-0.5465` n `239`; crypto_major avg `-0.5321` n `8`; equity avg `-0.227` n `158`; fx avg `-0.0048` n `6`; index avg `-0.1092` n `27`; metal avg `-0.0397` n `20`; unknown avg `15.9317` n `1237`
- 24h: commodity avg `0.0703` n `13`; crypto_alt avg `0.6685` n `239`; crypto_major avg `-0.9635` n `8`; equity avg `1.7789` n `158`; fx avg `-0.0945` n `6`; index avg `0.2053` n `27`; metal avg `-0.1467` n `20`; unknown avg `62.254` n `1086`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
