# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T13:07:35.856946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `0.2068` n `234`; crypto_major avg `0.0031` n `8`; equity avg `0.0238` n `141`; fx avg `0.0078` n `6`; index avg `0.0061` n `26`; metal avg `0.0112` n `20`; unknown avg `2.6763` n `961`
- 1h: commodity avg `-0.1643` n `12`; crypto_alt avg `0.0036` n `234`; crypto_major avg `0.3935` n `8`; equity avg `-0.0387` n `141`; fx avg `0.0009` n `6`; index avg `-0.0341` n `26`; metal avg `-0.1255` n `20`; unknown avg `0.0585` n `961`
- 4h: commodity avg `-0.3932` n `12`; crypto_alt avg `1.3127` n `234`; crypto_major avg `1.1302` n `8`; equity avg `0.4035` n `141`; fx avg `-0.0408` n `6`; index avg `0.0526` n `26`; metal avg `0.0488` n `20`; unknown avg `0.3081` n `955`
- 24h: commodity avg `-0.777` n `12`; crypto_alt avg `1.1909` n `234`; crypto_major avg `0.8067` n `8`; equity avg `-0.0654` n `141`; fx avg `-0.106` n `6`; index avg `-0.0408` n `26`; metal avg `-0.1295` n `20`; unknown avg `81.4343` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
