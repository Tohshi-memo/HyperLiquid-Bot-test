# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T03:07:25.009009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0445` n `13`; crypto_alt avg `-0.2065` n `239`; crypto_major avg `-0.1866` n `8`; equity avg `-0.226` n `164`; fx avg `-0.0077` n `6`; index avg `-0.0293` n `27`; metal avg `-0.18` n `20`; unknown avg `-0.057` n `1259`
- 1h: commodity avg `-0.1377` n `13`; crypto_alt avg `-0.3055` n `239`; crypto_major avg `-0.3829` n `8`; equity avg `-0.2925` n `164`; fx avg `-0.0318` n `6`; index avg `-0.0457` n `27`; metal avg `-0.3573` n `20`; unknown avg `-0.2975` n `1263`
- 4h: commodity avg `0.0545` n `13`; crypto_alt avg `0.2077` n `239`; crypto_major avg `-0.1748` n `8`; equity avg `0.0347` n `164`; fx avg `-0.0545` n `6`; index avg `-0.0367` n `27`; metal avg `-0.2904` n `20`; unknown avg `2.258` n `1255`
- 24h: commodity avg `-0.0587` n `13`; crypto_alt avg `-0.6362` n `239`; crypto_major avg `-2.0896` n `8`; equity avg `-0.6765` n `164`; fx avg `-0.1194` n `6`; index avg `0.0013` n `27`; metal avg `-0.8589` n `20`; unknown avg `90.8404` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
