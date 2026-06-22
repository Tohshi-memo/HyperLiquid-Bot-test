# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T05:52:26.518599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.1125` n `228`; crypto_major avg `-0.1289` n `8`; equity avg `-0.0118` n `79`; fx avg `-0.0009` n `6`; index avg `-0.0158` n `23`; metal avg `0.0351` n `18`; unknown avg `4.2075` n `701`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.0114` n `228`; crypto_major avg `0.1359` n `8`; equity avg `0.0939` n `79`; fx avg `-0.0084` n `6`; index avg `0.0314` n `23`; metal avg `0.3177` n `18`; unknown avg `0.8417` n `701`
- 4h: commodity avg `-0.1208` n `12`; crypto_alt avg `-0.7159` n `228`; crypto_major avg `-0.9198` n `8`; equity avg `0.0767` n `79`; fx avg `-0.0195` n `6`; index avg `-0.0406` n `23`; metal avg `0.1246` n `18`; unknown avg `0.1992` n `701`
- 24h: commodity avg `-0.3904` n `12`; crypto_alt avg `0.2418` n `228`; crypto_major avg `-0.4806` n `8`; equity avg `-0.5685` n `79`; fx avg `0.0018` n `6`; index avg `-0.0319` n `23`; metal avg `0.4405` n `18`; unknown avg `-0.4687` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
