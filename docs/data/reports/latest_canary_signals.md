# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T06:07:28.344451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `-0.0826` n `234`; crypto_major avg `0.0204` n `8`; equity avg `0.0419` n `141`; fx avg `0.0165` n `6`; index avg `0.0006` n `26`; metal avg `-0.0211` n `20`; unknown avg `-0.0391` n `912`
- 1h: commodity avg `-0.1015` n `12`; crypto_alt avg `0.1534` n `234`; crypto_major avg `0.1151` n `8`; equity avg `0.215` n `141`; fx avg `-0.0035` n `6`; index avg `0.0493` n `26`; metal avg `0.054` n `20`; unknown avg `-0.0073` n `912`
- 4h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.7494` n `234`; crypto_major avg `-0.7693` n `8`; equity avg `0.2396` n `141`; fx avg `-0.0442` n `6`; index avg `0.0593` n `26`; metal avg `-0.1454` n `20`; unknown avg `1.892` n `906`
- 24h: commodity avg `0.2514` n `12`; crypto_alt avg `1.7741` n `234`; crypto_major avg `0.4898` n `8`; equity avg `0.9227` n `141`; fx avg `-0.1239` n `6`; index avg `0.138` n `26`; metal avg `-0.1694` n `20`; unknown avg `13.0779` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
