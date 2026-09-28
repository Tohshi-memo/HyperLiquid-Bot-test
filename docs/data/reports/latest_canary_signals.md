# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T14:22:34.064495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.1228` n `234`; crypto_major avg `-0.0603` n `8`; equity avg `-0.0515` n `141`; fx avg `0.0131` n `6`; index avg `0.0046` n `26`; metal avg `-0.0146` n `20`; unknown avg `0.5829` n `946`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.4352` n `234`; crypto_major avg `-0.2002` n `8`; equity avg `-0.3726` n `141`; fx avg `0.0194` n `6`; index avg `-0.0604` n `26`; metal avg `0.0299` n `20`; unknown avg `109.1079` n `918`
- 4h: commodity avg `-0.2769` n `12`; crypto_alt avg `0.8509` n `234`; crypto_major avg `0.7975` n `8`; equity avg `-0.0288` n `141`; fx avg `0.0016` n `6`; index avg `0.0276` n `26`; metal avg `-0.0729` n `20`; unknown avg `240.8262` n `912`
- 24h: commodity avg `-0.2941` n `12`; crypto_alt avg `-2.9276` n `234`; crypto_major avg `-1.9313` n `8`; equity avg `-2.8415` n `141`; fx avg `0.0326` n `6`; index avg `-0.235` n `26`; metal avg `-0.9587` n `20`; unknown avg `5.9182` n `794`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
