# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T23:21:22.578756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.0043` n `230`; crypto_major avg `-0.0321` n `8`; equity avg `-0.1302` n `113`; fx avg `-0.0008` n `6`; index avg `-0.0025` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0285` n `786`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.1334` n `230`; crypto_major avg `-0.2609` n `8`; equity avg `0.0853` n `113`; fx avg `-0.0058` n `6`; index avg `-0.002` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.0984` n `786`
- 4h: commodity avg `-0.0494` n `12`; crypto_alt avg `0.3555` n `230`; crypto_major avg `0.7658` n `8`; equity avg `0.6258` n `113`; fx avg `-0.0074` n `6`; index avg `0.0367` n `25`; metal avg `0.0629` n `20`; unknown avg `0.3312` n `785`
- 24h: commodity avg `0.1696` n `12`; crypto_alt avg `-1.1145` n `230`; crypto_major avg `0.5981` n `8`; equity avg `1.5361` n `113`; fx avg `-0.0728` n `6`; index avg `0.13` n `25`; metal avg `-0.2086` n `20`; unknown avg `-0.0951` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.214`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
