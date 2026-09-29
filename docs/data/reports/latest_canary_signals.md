# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T10:52:25.578308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `0.2332` n `234`; crypto_major avg `0.0833` n `8`; equity avg `0.0664` n `141`; fx avg `-0.0091` n `6`; index avg `0.0101` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.1783` n `963`
- 1h: commodity avg `-0.0909` n `12`; crypto_alt avg `-0.0163` n `234`; crypto_major avg `-0.2289` n `8`; equity avg `0.1636` n `141`; fx avg `-0.0194` n `6`; index avg `0.0405` n `26`; metal avg `0.0379` n `20`; unknown avg `0.3151` n `961`
- 4h: commodity avg `-0.4908` n `12`; crypto_alt avg `1.1677` n `234`; crypto_major avg `0.2502` n `8`; equity avg `0.4799` n `141`; fx avg `-0.0696` n `6`; index avg `0.0335` n `26`; metal avg `0.0405` n `20`; unknown avg `0.035` n `945`
- 24h: commodity avg `-0.7389` n `12`; crypto_alt avg `1.3415` n `234`; crypto_major avg `0.6651` n `8`; equity avg `-0.0423` n `141`; fx avg `-0.1031` n `6`; index avg `-0.0075` n `26`; metal avg `-0.2322` n `20`; unknown avg `38.8922` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
