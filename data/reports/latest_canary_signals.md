# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T16:52:28.898338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0597` n `12`; crypto_alt avg `0.0565` n `230`; crypto_major avg `-0.0759` n `8`; equity avg `-0.0687` n `103`; fx avg `-0.0043` n `6`; index avg `0.0072` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.0005` n `784`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.104` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `0.0533` n `103`; fx avg `-0.0111` n `6`; index avg `0.0263` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0479` n `784`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `1.03` n `230`; crypto_major avg `1.3511` n `8`; equity avg `2.4581` n `103`; fx avg `-0.0268` n `6`; index avg `0.2215` n `25`; metal avg `0.0434` n `20`; unknown avg `0.0524` n `784`
- 24h: commodity avg `-0.1657` n `12`; crypto_alt avg `0.27` n `230`; crypto_major avg `0.8016` n `8`; equity avg `1.3679` n `102`; fx avg `-0.1763` n `6`; index avg `-0.0201` n `25`; metal avg `-0.4502` n `20`; unknown avg `0.0884` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
