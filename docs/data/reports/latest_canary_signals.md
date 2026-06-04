# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T04:37:23.591111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.7958` n `228`; crypto_major avg `-0.5802` n `8`; equity avg `0.0483` n `73`; fx avg `-0.0149` n `6`; index avg `0.0667` n `23`; metal avg `0.112` n `18`; unknown avg `1.8114` n `420`
- 1h: commodity avg `0.1039` n `12`; crypto_alt avg `-0.6436` n `228`; crypto_major avg `-0.0091` n `8`; equity avg `0.1082` n `73`; fx avg `-0.0029` n `6`; index avg `0.0733` n `23`; metal avg `0.3097` n `18`; unknown avg `0.9058` n `420`
- 4h: commodity avg `-0.2035` n `12`; crypto_alt avg `-1.8733` n `228`; crypto_major avg `0.5605` n `8`; equity avg `0.2056` n `73`; fx avg `-0.0021` n `6`; index avg `0.0081` n `23`; metal avg `0.6055` n `18`; unknown avg `1.4319` n `419`
- 24h: commodity avg `0.0266` n `12`; crypto_alt avg `-1.6305` n `228`; crypto_major avg `-1.2688` n `8`; equity avg `-3.3321` n `73`; fx avg `-0.0087` n `6`; index avg `-1.0905` n `23`; metal avg `-1.2236` n `18`; unknown avg `0.7737` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
