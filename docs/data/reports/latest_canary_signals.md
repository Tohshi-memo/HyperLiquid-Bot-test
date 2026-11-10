# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T23:22:36.654354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `13`; crypto_alt avg `0.2809` n `239`; crypto_major avg `0.2202` n `8`; equity avg `0.3418` n `160`; fx avg `-0.0099` n `6`; index avg `0.0396` n `27`; metal avg `0.0117` n `20`; unknown avg `-0.0312` n `1262`
- 1h: commodity avg `-0.0619` n `13`; crypto_alt avg `-0.0651` n `239`; crypto_major avg `-0.268` n `8`; equity avg `0.4347` n `160`; fx avg `0.0018` n `6`; index avg `0.0501` n `27`; metal avg `0.0223` n `20`; unknown avg `18.7624` n `1256`
- 4h: commodity avg `0.0206` n `13`; crypto_alt avg `0.6438` n `239`; crypto_major avg `0.3429` n `8`; equity avg `1.2014` n `160`; fx avg `-0.0098` n `6`; index avg `0.1058` n `27`; metal avg `0.0532` n `20`; unknown avg `20.6143` n `1226`
- 24h: commodity avg `0.1158` n `13`; crypto_alt avg `-0.8227` n `239`; crypto_major avg `-2.7823` n `8`; equity avg `-1.0589` n `160`; fx avg `-0.1272` n `6`; index avg `-0.167` n `27`; metal avg `-0.6709` n `20`; unknown avg `20.8819` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.258`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
