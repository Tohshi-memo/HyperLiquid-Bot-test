# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T10:37:26.862622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `0.0746` n `234`; crypto_major avg `0.0335` n `8`; equity avg `0.0363` n `137`; fx avg `0.0073` n `6`; index avg `0.0143` n `27`; metal avg `0.0228` n `20`; unknown avg `11.9098` n `919`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `0.0943` n `234`; crypto_major avg `0.0509` n `8`; equity avg `0.008` n `137`; fx avg `-0.0116` n `6`; index avg `0.022` n `27`; metal avg `0.0906` n `20`; unknown avg `1.9011` n `917`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.0915` n `234`; crypto_major avg `0.2036` n `8`; equity avg `0.1764` n `137`; fx avg `-0.013` n `6`; index avg `0.019` n `27`; metal avg `0.043` n `20`; unknown avg `0.6022` n `911`
- 24h: commodity avg `0.1517` n `12`; crypto_alt avg `-2.7957` n `234`; crypto_major avg `-2.7602` n `8`; equity avg `-0.205` n `137`; fx avg `0.1131` n `6`; index avg `0.0932` n `27`; metal avg `0.5397` n `20`; unknown avg `18892.2212` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
