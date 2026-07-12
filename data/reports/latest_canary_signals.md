# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T10:37:31.280152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0044` n `230`; crypto_major avg `-0.0549` n `8`; equity avg `-0.0379` n `92`; fx avg `-0.0001` n `6`; index avg `-0.0097` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.1154` n `765`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.0335` n `230`; crypto_major avg `-0.0266` n `8`; equity avg `0.0073` n `92`; fx avg `0.0037` n `6`; index avg `0.0031` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.1835` n `765`
- 4h: commodity avg `0.1097` n `12`; crypto_alt avg `0.1792` n `230`; crypto_major avg `0.2749` n `8`; equity avg `0.0315` n `92`; fx avg `0.007` n `6`; index avg `0.0193` n `25`; metal avg `-0.0107` n `20`; unknown avg `1.6844` n `763`
- 24h: commodity avg `0.4959` n `12`; crypto_alt avg `-0.8035` n `230`; crypto_major avg `-0.6784` n `8`; equity avg `-0.1887` n `92`; fx avg `0.008` n `6`; index avg `-0.1241` n `25`; metal avg `-0.1145` n `20`; unknown avg `0.0309` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
