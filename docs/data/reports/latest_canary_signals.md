# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T16:07:30.558109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3041` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0251` n `12`; crypto_alt avg `0.086` n `234`; crypto_major avg `0.0942` n `8`; equity avg `0.0727` n `141`; fx avg `-0.023` n `6`; index avg `0.0089` n `26`; metal avg `-0.0483` n `20`; unknown avg `-0.3111` n `955`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-1.0227` n `234`; crypto_major avg `-0.6858` n `8`; equity avg `-0.2406` n `141`; fx avg `-0.0527` n `6`; index avg `-0.0411` n `26`; metal avg `-0.1022` n `20`; unknown avg `1.7012` n `951`
- 4h: commodity avg `-0.1023` n `12`; crypto_alt avg `-1.299` n `234`; crypto_major avg `-1.4053` n `8`; equity avg `-0.0273` n `141`; fx avg `-0.0274` n `6`; index avg `-0.1012` n `26`; metal avg `-0.2239` n `20`; unknown avg `4.1125` n `893`
- 24h: commodity avg `-0.6974` n `12`; crypto_alt avg `1.2324` n `234`; crypto_major avg `-0.3984` n `8`; equity avg `0.9104` n `141`; fx avg `-0.1636` n `6`; index avg `0.0612` n `26`; metal avg `-0.0897` n `20`; unknown avg `18.6339` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
