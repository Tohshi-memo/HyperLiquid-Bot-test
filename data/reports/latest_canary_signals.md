# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T02:52:27.547532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.1936` n `239`; crypto_major avg `-0.1264` n `8`; equity avg `0.0046` n `158`; fx avg `-0.0015` n `6`; index avg `0.0086` n `27`; metal avg `-0.0003` n `20`; unknown avg `0.1406` n `1260`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `-0.2256` n `239`; crypto_major avg `-0.2096` n `8`; equity avg `-0.0231` n `158`; fx avg `-0.008` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0069` n `20`; unknown avg `-0.2462` n `1254`
- 4h: commodity avg `-0.0482` n `13`; crypto_alt avg `-0.6671` n `239`; crypto_major avg `-0.2318` n `8`; equity avg `-0.0222` n `158`; fx avg `0.0234` n `6`; index avg `0.0052` n `27`; metal avg `-0.0191` n `20`; unknown avg `0.0522` n `1230`
- 24h: commodity avg `0.0652` n `13`; crypto_alt avg `-1.9933` n `239`; crypto_major avg `-1.0496` n `8`; equity avg `-0.0506` n `158`; fx avg `0.0129` n `6`; index avg `0.0404` n `27`; metal avg `-0.0493` n `20`; unknown avg `161.2845` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
