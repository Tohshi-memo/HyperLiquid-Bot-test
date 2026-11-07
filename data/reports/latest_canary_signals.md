# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T04:22:27.301395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.0676` n `239`; crypto_major avg `-0.0592` n `8`; equity avg `-0.0163` n `158`; fx avg `-0.0013` n `6`; index avg `-0.0005` n `27`; metal avg `0.0007` n `20`; unknown avg `-0.0931` n `1259`
- 1h: commodity avg `-0.1124` n `13`; crypto_alt avg `-0.0795` n `239`; crypto_major avg `-0.1606` n `8`; equity avg `-0.0343` n `158`; fx avg `0.0159` n `6`; index avg `0.0088` n `27`; metal avg `-0.0041` n `20`; unknown avg `0.477` n `1243`
- 4h: commodity avg `-0.1515` n `13`; crypto_alt avg `-0.3414` n `239`; crypto_major avg `-0.3158` n `8`; equity avg `0.0419` n `158`; fx avg `0.0085` n `6`; index avg `0.017` n `27`; metal avg `0.0082` n `20`; unknown avg `0.981` n `1241`
- 24h: commodity avg `-0.3796` n `13`; crypto_alt avg `0.4106` n `239`; crypto_major avg `0.1617` n `8`; equity avg `1.348` n `158`; fx avg `-0.041` n `6`; index avg `0.1788` n `27`; metal avg `0.2777` n `20`; unknown avg `8.2614` n `1016`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
