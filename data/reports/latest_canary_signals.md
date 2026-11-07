# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T02:37:26.980881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.1031` n `239`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0201` n `158`; fx avg `-0.0007` n `6`; index avg `0.001` n `27`; metal avg `0.0069` n `20`; unknown avg `-0.1203` n `1261`
- 1h: commodity avg `-0.034` n `13`; crypto_alt avg `-0.1652` n `239`; crypto_major avg `-0.0503` n `8`; equity avg `0.0493` n `158`; fx avg `0.0054` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0074` n `20`; unknown avg `-0.3583` n `1255`
- 4h: commodity avg `-0.0608` n `13`; crypto_alt avg `-0.1331` n `239`; crypto_major avg `0.0238` n `8`; equity avg `-0.0673` n `158`; fx avg `0.0031` n `6`; index avg `0.0104` n `27`; metal avg `0.0092` n `20`; unknown avg `-0.1469` n `1233`
- 24h: commodity avg `-0.2596` n `13`; crypto_alt avg `0.4893` n `239`; crypto_major avg `-0.2615` n `8`; equity avg `0.4528` n `158`; fx avg `-0.0756` n `6`; index avg `0.0438` n `27`; metal avg `0.0269` n `20`; unknown avg `7.9466` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
