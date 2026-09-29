# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T13:22:38.913914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `12`; crypto_alt avg `0.0856` n `234`; crypto_major avg `0.0769` n `8`; equity avg `0.0424` n `141`; fx avg `0.015` n `6`; index avg `0.0079` n `26`; metal avg `-0.007` n `20`; unknown avg `2.1263` n `963`
- 1h: commodity avg `-0.2274` n `12`; crypto_alt avg `0.1091` n `234`; crypto_major avg `0.5147` n `8`; equity avg `0.0603` n `141`; fx avg `0.0058` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0645` n `20`; unknown avg `0.8661` n `961`
- 4h: commodity avg `-0.4474` n `12`; crypto_alt avg `1.2987` n `234`; crypto_major avg `1.0964` n `8`; equity avg `0.4803` n `141`; fx avg `-0.0087` n `6`; index avg `0.0704` n `26`; metal avg `0.026` n `20`; unknown avg `0.1793` n `955`
- 24h: commodity avg `-0.7914` n `12`; crypto_alt avg `1.504` n `234`; crypto_major avg `1.0187` n `8`; equity avg `0.0371` n `141`; fx avg `-0.0874` n `6`; index avg `-0.0266` n `26`; metal avg `-0.102` n `20`; unknown avg `108.458` n `808`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
