# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T17:37:30.092742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `-0.3089` n `230`; crypto_major avg `-0.3436` n `8`; equity avg `-0.0064` n `102`; fx avg `-0.005` n `6`; index avg `-0.002` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.052` n `782`
- 1h: commodity avg `0.0619` n `12`; crypto_alt avg `-0.6565` n `230`; crypto_major avg `-0.6551` n `8`; equity avg `-0.0369` n `102`; fx avg `-0.007` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0682` n `782`
- 4h: commodity avg `0.078` n `12`; crypto_alt avg `-0.5112` n `230`; crypto_major avg `-0.635` n `8`; equity avg `-0.1349` n `102`; fx avg `-0.0101` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0026` n `20`; unknown avg `-0.0728` n `782`
- 24h: commodity avg `0.6902` n `12`; crypto_alt avg `-0.6843` n `230`; crypto_major avg `-1.2745` n `8`; equity avg `-1.3684` n `102`; fx avg `-0.0633` n `6`; index avg `-0.1534` n `25`; metal avg `-0.0467` n `20`; unknown avg `4.2139` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
