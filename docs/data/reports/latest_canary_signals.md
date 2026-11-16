# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T09:37:24.932349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `13`; crypto_alt avg `0.1064` n `239`; crypto_major avg `0.1836` n `8`; equity avg `0.1242` n `162`; fx avg `-0.0366` n `6`; index avg `0.0204` n `27`; metal avg `-0.0632` n `20`; unknown avg `0.1251` n `1265`
- 1h: commodity avg `-0.2447` n `13`; crypto_alt avg `0.0167` n `239`; crypto_major avg `-0.2237` n `8`; equity avg `-0.183` n `162`; fx avg `-0.0179` n `6`; index avg `-0.0009` n `27`; metal avg `0.0014` n `20`; unknown avg `9.3724` n `1261`
- 4h: commodity avg `-0.2321` n `13`; crypto_alt avg `-0.3102` n `239`; crypto_major avg `-0.4574` n `8`; equity avg `-0.1318` n `162`; fx avg `-0.0305` n `6`; index avg `0.0507` n `27`; metal avg `-0.1093` n `20`; unknown avg `12.9747` n `1077`
- 24h: commodity avg `-0.546` n `13`; crypto_alt avg `-1.0199` n `239`; crypto_major avg `-1.0588` n `8`; equity avg `-0.7623` n `162`; fx avg `-0.0907` n `6`; index avg `-0.0219` n `27`; metal avg `-0.051` n `20`; unknown avg `13.2131` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
