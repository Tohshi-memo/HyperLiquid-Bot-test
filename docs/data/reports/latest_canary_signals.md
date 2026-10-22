# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T22:07:28.862539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0449` n `13`; crypto_alt avg `0.2039` n `237`; crypto_major avg `0.0976` n `8`; equity avg `0.158` n `151`; fx avg `-0.0068` n `6`; index avg `0.0569` n `26`; metal avg `0.0063` n `20`; unknown avg `0.1311` n `1231`
- 1h: commodity avg `0.0225` n `13`; crypto_alt avg `0.3054` n `237`; crypto_major avg `0.1992` n `8`; equity avg `0.0834` n `151`; fx avg `0.0061` n `6`; index avg `0.0342` n `26`; metal avg `0.0225` n `20`; unknown avg `0.9187` n `1231`
- 4h: commodity avg `-0.0591` n `13`; crypto_alt avg `0.351` n `237`; crypto_major avg `0.4635` n `8`; equity avg `0.0285` n `151`; fx avg `-0.0441` n `6`; index avg `0.0071` n `26`; metal avg `-0.0573` n `20`; unknown avg `-0.1132` n `1167`
- 24h: commodity avg `0.5564` n `13`; crypto_alt avg `-5.1299` n `237`; crypto_major avg `-3.7896` n `8`; equity avg `-5.8072` n `151`; fx avg `-0.1903` n `6`; index avg `-0.6844` n `26`; metal avg `-0.9595` n `20`; unknown avg `60.1243` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
