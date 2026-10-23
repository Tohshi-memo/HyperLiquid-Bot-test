# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T15:37:34.951905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1038` n `13`; crypto_alt avg `-0.1663` n `237`; crypto_major avg `-0.086` n `8`; equity avg `0.0635` n `152`; fx avg `0.0171` n `6`; index avg `0.0146` n `26`; metal avg `-0.0243` n `20`; unknown avg `-0.1667` n `1233`
- 1h: commodity avg `-0.0688` n `13`; crypto_alt avg `-0.2225` n `237`; crypto_major avg `-0.1318` n `8`; equity avg `0.1737` n `152`; fx avg `-0.0065` n `6`; index avg `0.0933` n `26`; metal avg `0.1125` n `20`; unknown avg `0.2721` n `1231`
- 4h: commodity avg `0.1043` n `13`; crypto_alt avg `-0.3619` n `237`; crypto_major avg `-0.0464` n `8`; equity avg `0.3337` n `152`; fx avg `0.0288` n `6`; index avg `0.1032` n `26`; metal avg `-0.0262` n `20`; unknown avg `-0.3284` n `1161`
- 24h: commodity avg `0.5018` n `13`; crypto_alt avg `0.4171` n `237`; crypto_major avg `0.234` n `8`; equity avg `0.6469` n `152`; fx avg `-0.0564` n `6`; index avg `0.0208` n `26`; metal avg `-0.2577` n `20`; unknown avg `-0.6528` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
