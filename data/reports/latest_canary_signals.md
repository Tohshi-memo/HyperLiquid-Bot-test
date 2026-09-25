# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T17:07:31.409981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1133` n `12`; crypto_alt avg `0.0115` n `234`; crypto_major avg `-0.0615` n `8`; equity avg `0.0062` n `141`; fx avg `0.0036` n `6`; index avg `0.0066` n `26`; metal avg `0.0313` n `20`; unknown avg `-0.2085` n `958`
- 1h: commodity avg `-0.0834` n `12`; crypto_alt avg `0.2679` n `234`; crypto_major avg `-0.0943` n `8`; equity avg `-0.131` n `141`; fx avg `0.0219` n `6`; index avg `-0.0315` n `26`; metal avg `-0.0481` n `20`; unknown avg `2.9862` n `954`
- 4h: commodity avg `-0.3729` n `12`; crypto_alt avg `-0.4423` n `234`; crypto_major avg `-0.9353` n `8`; equity avg `-0.6222` n `141`; fx avg `-0.0352` n `6`; index avg `0.0294` n `26`; metal avg `0.0524` n `20`; unknown avg `8.3102` n `894`
- 24h: commodity avg `-0.8202` n `12`; crypto_alt avg `1.7266` n `234`; crypto_major avg `0.5837` n `8`; equity avg `-0.0403` n `141`; fx avg `-0.2414` n `6`; index avg `0.1242` n `26`; metal avg `0.1412` n `20`; unknown avg `1601.5654` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
