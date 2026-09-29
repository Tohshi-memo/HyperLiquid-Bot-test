# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T04:22:28.420084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.8081` n `234`; crypto_major avg `0.4243` n `8`; equity avg `0.0596` n `141`; fx avg `-0.0095` n `6`; index avg `0.0053` n `26`; metal avg `0.0065` n `20`; unknown avg `12.1295` n `963`
- 1h: commodity avg `0.0306` n `12`; crypto_alt avg `0.694` n `234`; crypto_major avg `0.4163` n `8`; equity avg `-0.0384` n `141`; fx avg `-0.0187` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0882` n `20`; unknown avg `11.7961` n `955`
- 4h: commodity avg `0.1813` n `12`; crypto_alt avg `-0.8494` n `234`; crypto_major avg `-0.1906` n `8`; equity avg `-0.4675` n `141`; fx avg `-0.044` n `6`; index avg `-0.0902` n `26`; metal avg `-0.0436` n `20`; unknown avg `0.3567` n `955`
- 24h: commodity avg `0.1225` n `12`; crypto_alt avg `-2.3613` n `234`; crypto_major avg `-0.9277` n `8`; equity avg `-2.2522` n `141`; fx avg `-0.0534` n `6`; index avg `-0.2557` n `26`; metal avg `-0.5409` n `20`; unknown avg `8.2353` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
