# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T23:07:30.304563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.2012` n `234`; crypto_major avg `0.2344` n `8`; equity avg `0.0326` n `140`; fx avg `0.0001` n `6`; index avg `0.0078` n `26`; metal avg `0.0222` n `20`; unknown avg `-0.1524` n `917`
- 1h: commodity avg `0.0338` n `12`; crypto_alt avg `0.3798` n `234`; crypto_major avg `0.2708` n `8`; equity avg `-0.029` n `140`; fx avg `-0.0038` n `6`; index avg `-0.0083` n `26`; metal avg `0.0168` n `20`; unknown avg `0.8428` n `851`
- 4h: commodity avg `-0.0498` n `12`; crypto_alt avg `0.4258` n `234`; crypto_major avg `0.5473` n `8`; equity avg `-0.0158` n `140`; fx avg `-0.0009` n `6`; index avg `-0.0408` n `26`; metal avg `-0.0528` n `20`; unknown avg `0.1556` n `791`
- 24h: commodity avg `-0.1817` n `12`; crypto_alt avg `4.4682` n `234`; crypto_major avg `2.6652` n `8`; equity avg `1.9788` n `138`; fx avg `-0.0009` n `6`; index avg `0.3641` n `26`; metal avg `0.5968` n `20`; unknown avg `2.6336` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
