# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T19:07:27.930542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0145` n `13`; crypto_alt avg `0.1932` n `239`; crypto_major avg `0.1005` n `8`; equity avg `0.0283` n `162`; fx avg `-0.0015` n `6`; index avg `0.0119` n `27`; metal avg `0.0166` n `20`; unknown avg `0.0255` n `1257`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `0.1158` n `239`; crypto_major avg `-0.1787` n `8`; equity avg `-0.3166` n `162`; fx avg `0.0058` n `6`; index avg `-0.025` n `27`; metal avg `-0.0065` n `20`; unknown avg `0.1413` n `1255`
- 4h: commodity avg `0.3596` n `13`; crypto_alt avg `0.8985` n `239`; crypto_major avg `0.5956` n `8`; equity avg `1.1169` n `162`; fx avg `-0.0475` n `6`; index avg `0.0931` n `27`; metal avg `0.1442` n `20`; unknown avg `65.7215` n `1229`
- 24h: commodity avg `0.5009` n `13`; crypto_alt avg `-2.6242` n `239`; crypto_major avg `-3.1046` n `8`; equity avg `-2.9146` n `162`; fx avg `-0.1547` n `6`; index avg `-0.1825` n `27`; metal avg `-0.738` n `20`; unknown avg `19.4706` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
