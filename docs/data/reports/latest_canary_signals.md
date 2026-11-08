# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T08:07:34.023411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `-0.155` n `239`; crypto_major avg `-0.0849` n `8`; equity avg `-0.0338` n `158`; fx avg `0.0046` n `6`; index avg `-0.0173` n `27`; metal avg `0.0048` n `20`; unknown avg `201.9495` n `1244`
- 1h: commodity avg `0.0302` n `13`; crypto_alt avg `0.0314` n `239`; crypto_major avg `0.1115` n `8`; equity avg `0.0581` n `158`; fx avg `0.0049` n `6`; index avg `0.0175` n `27`; metal avg `0.0069` n `20`; unknown avg `202.7308` n `1240`
- 4h: commodity avg `0.0387` n `13`; crypto_alt avg `-0.2138` n `239`; crypto_major avg `-0.0068` n `8`; equity avg `0.1047` n `158`; fx avg `0.0179` n `6`; index avg `0.0173` n `27`; metal avg `0.0088` n `20`; unknown avg `0.9508` n `1198`
- 24h: commodity avg `0.1421` n `13`; crypto_alt avg `-1.8401` n `239`; crypto_major avg `-0.7083` n `8`; equity avg `0.0628` n `158`; fx avg `0.0639` n `6`; index avg `0.0401` n `27`; metal avg `-0.0314` n `20`; unknown avg `159.6552` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
