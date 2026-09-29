# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T12:07:37.454309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.1006` n `234`; crypto_major avg `-0.0944` n `8`; equity avg `0.0597` n `141`; fx avg `-0.0169` n `6`; index avg `0.0139` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.1169` n `955`
- 1h: commodity avg `-0.1003` n `12`; crypto_alt avg `0.6795` n `234`; crypto_major avg `0.348` n `8`; equity avg `0.1556` n `141`; fx avg `-0.01` n `6`; index avg `0.0245` n `26`; metal avg `0.0787` n `20`; unknown avg `211.4933` n `955`
- 4h: commodity avg `-0.4776` n `12`; crypto_alt avg `1.3604` n `234`; crypto_major avg `0.4747` n `8`; equity avg `0.517` n `141`; fx avg `-0.0635` n `6`; index avg `0.0965` n `26`; metal avg `0.2311` n `20`; unknown avg `169.7435` n `955`
- 24h: commodity avg `-0.7413` n `12`; crypto_alt avg `1.2045` n `234`; crypto_major avg `0.3879` n `8`; equity avg `-0.1502` n `141`; fx avg `-0.0837` n `6`; index avg `-0.0123` n `26`; metal avg `-0.188` n `20`; unknown avg `61.0711` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
