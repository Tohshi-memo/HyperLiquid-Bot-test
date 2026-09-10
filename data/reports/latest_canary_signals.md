# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T22:07:30.680446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2171` n `12`; crypto_alt avg `-0.1437` n `233`; crypto_major avg `-0.043` n `8`; equity avg `0.0379` n `136`; fx avg `0.018` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0126` n `20`; unknown avg `0.239` n `762`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.3763` n `233`; crypto_major avg `-0.2073` n `8`; equity avg `-0.1112` n `136`; fx avg `0.0192` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0243` n `20`; unknown avg `0.5916` n `762`
- 4h: commodity avg `0.2681` n `12`; crypto_alt avg `0.0306` n `233`; crypto_major avg `0.1716` n `8`; equity avg `-0.4427` n `136`; fx avg `0.0362` n `6`; index avg `-0.0168` n `26`; metal avg `-0.1417` n `20`; unknown avg `-0.171` n `718`
- 24h: commodity avg `1.145` n `12`; crypto_alt avg `-1.9021` n `233`; crypto_major avg `-1.5509` n `8`; equity avg `-2.0003` n `136`; fx avg `0.1427` n `6`; index avg `-0.3355` n `26`; metal avg `-1.2801` n `20`; unknown avg `-0.8253` n `653`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
