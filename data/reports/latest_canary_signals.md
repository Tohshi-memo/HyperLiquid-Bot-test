# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T15:07:30.095542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `13`; crypto_alt avg `-0.2631` n `235`; crypto_major avg `-0.2826` n `8`; equity avg `-0.0921` n `150`; fx avg `-0.0146` n `6`; index avg `-0.0252` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.0052` n `1076`
- 1h: commodity avg `0.1595` n `13`; crypto_alt avg `0.0347` n `235`; crypto_major avg `-0.0453` n `8`; equity avg `-0.0085` n `150`; fx avg `-0.0068` n `6`; index avg `-0.0206` n `26`; metal avg `-0.0582` n `20`; unknown avg `-0.0953` n `1076`
- 4h: commodity avg `0.5051` n `13`; crypto_alt avg `-0.0964` n `235`; crypto_major avg `-0.1479` n `8`; equity avg `-0.4749` n `150`; fx avg `0.0061` n `6`; index avg `-0.0729` n `26`; metal avg `0.0602` n `20`; unknown avg `1.0086` n `1022`
- 24h: commodity avg `0.0091` n `13`; crypto_alt avg `-1.0758` n `235`; crypto_major avg `-1.0444` n `8`; equity avg `-0.3501` n `150`; fx avg `-0.0062` n `6`; index avg `-0.0132` n `26`; metal avg `0.6486` n `20`; unknown avg `30.2869` n `955`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
