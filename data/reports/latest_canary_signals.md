# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T11:37:30.052099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `0.3753` n `234`; crypto_major avg `0.2438` n `8`; equity avg `0.0448` n `141`; fx avg `0.0083` n `6`; index avg `0.0168` n `26`; metal avg `0.0249` n `20`; unknown avg `-0.074` n `963`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `0.6715` n `234`; crypto_major avg `0.3138` n `8`; equity avg `0.182` n `141`; fx avg `-0.0043` n `6`; index avg `0.0495` n `26`; metal avg `0.1123` n `20`; unknown avg `-0.0214` n `961`
- 4h: commodity avg `-0.3215` n `12`; crypto_alt avg `0.9244` n `234`; crypto_major avg `0.1207` n `8`; equity avg `0.3364` n `141`; fx avg `-0.0168` n `6`; index avg `0.0468` n `26`; metal avg `0.165` n `20`; unknown avg `-0.3411` n `945`
- 24h: commodity avg `-0.6924` n `12`; crypto_alt avg `1.7427` n `234`; crypto_major avg `0.7343` n `8`; equity avg `-0.1104` n `141`; fx avg `-0.0801` n `6`; index avg `0.0062` n `26`; metal avg `-0.0634` n `20`; unknown avg `60.3124` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
