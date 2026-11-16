# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T05:22:30.850213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `0.1677` n `239`; crypto_major avg `0.3662` n `8`; equity avg `0.2047` n `162`; fx avg `-0.0047` n `6`; index avg `0.0242` n `27`; metal avg `0.1142` n `20`; unknown avg `0.2644` n `1263`
- 1h: commodity avg `-0.0561` n `13`; crypto_alt avg `-0.2156` n `239`; crypto_major avg `-0.0473` n `8`; equity avg `-0.2726` n `162`; fx avg `-0.0155` n `6`; index avg `-0.0367` n `27`; metal avg `0.0843` n `20`; unknown avg `197.9496` n `1261`
- 4h: commodity avg `-0.0087` n `13`; crypto_alt avg `0.5952` n `239`; crypto_major avg `0.3991` n `8`; equity avg `-0.3835` n `162`; fx avg `-0.0609` n `6`; index avg `-0.0642` n `27`; metal avg `-0.0208` n `20`; unknown avg `-0.0551` n `1247`
- 24h: commodity avg `-0.363` n `13`; crypto_alt avg `-0.2376` n `239`; crypto_major avg `0.1281` n `8`; equity avg `-0.0898` n `162`; fx avg `-0.0618` n `6`; index avg `-0.0034` n `27`; metal avg `0.2596` n `20`; unknown avg `1.2093` n `1131`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
