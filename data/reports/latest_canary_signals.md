# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T08:07:25.852621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1551` n `12`; crypto_alt avg `0.5002` n `232`; crypto_major avg `0.5827` n `8`; equity avg `0.2571` n `133`; fx avg `-0.0396` n `6`; index avg `0.0625` n `26`; metal avg `0.1333` n `20`; unknown avg `-0.0331` n `790`
- 1h: commodity avg `-0.1209` n `12`; crypto_alt avg `0.1306` n `232`; crypto_major avg `0.0725` n `8`; equity avg `0.2948` n `133`; fx avg `0.0496` n `6`; index avg `0.059` n `26`; metal avg `0.178` n `20`; unknown avg `2.8937` n `790`
- 4h: commodity avg `-0.3251` n `12`; crypto_alt avg `0.7544` n `232`; crypto_major avg `0.4422` n `8`; equity avg `-0.1229` n `133`; fx avg `-0.0852` n `6`; index avg `-0.0575` n `26`; metal avg `0.1276` n `20`; unknown avg `-0.0844` n `754`
- 24h: commodity avg `0.0318` n `12`; crypto_alt avg `0.8973` n `232`; crypto_major avg `0.9915` n `8`; equity avg `1.5117` n `133`; fx avg `-0.3756` n `6`; index avg `0.1415` n `26`; metal avg `0.8787` n `20`; unknown avg `-0.2685` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0408`, n `668`, weak_sample_signal
