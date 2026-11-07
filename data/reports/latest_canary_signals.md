# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T07:07:24.696479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `13`; crypto_alt avg `0.0451` n `239`; crypto_major avg `-0.0225` n `8`; equity avg `0.0063` n `158`; fx avg `0.0059` n `6`; index avg `0.0051` n `27`; metal avg `-0.0036` n `20`; unknown avg `11.481` n `1257`
- 1h: commodity avg `0.0683` n `13`; crypto_alt avg `0.012` n `239`; crypto_major avg `-0.0255` n `8`; equity avg `-0.0184` n `158`; fx avg `-0.015` n `6`; index avg `0.0058` n `27`; metal avg `-0.0065` n `20`; unknown avg `11.5011` n `1251`
- 4h: commodity avg `-0.0454` n `13`; crypto_alt avg `-0.1471` n `239`; crypto_major avg `-0.2492` n `8`; equity avg `-0.0918` n `158`; fx avg `-0.0112` n `6`; index avg `0.0162` n `27`; metal avg `-0.0179` n `20`; unknown avg `12.1512` n `1203`
- 24h: commodity avg `-0.2251` n `13`; crypto_alt avg `0.5154` n `239`; crypto_major avg `0.6728` n `8`; equity avg `1.3909` n `158`; fx avg `-0.0041` n `6`; index avg `0.229` n `27`; metal avg `0.2563` n `20`; unknown avg `8.6455` n `1010`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
