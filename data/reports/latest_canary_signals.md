# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T04:22:31.567470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0278` n `13`; crypto_alt avg `0.495` n `239`; crypto_major avg `0.4297` n `8`; equity avg `0.0123` n `166`; fx avg `-0.0037` n `6`; index avg `0.0009` n `27`; metal avg `0.0345` n `20`; unknown avg `0.2872` n `1262`
- 1h: commodity avg `-0.028` n `13`; crypto_alt avg `1.0583` n `239`; crypto_major avg `1.2222` n `8`; equity avg `0.4384` n `166`; fx avg `-0.0038` n `6`; index avg `0.0427` n `27`; metal avg `-0.037` n `20`; unknown avg `345.8308` n `1246`
- 4h: commodity avg `-0.1435` n `13`; crypto_alt avg `-0.1605` n `239`; crypto_major avg `-0.2229` n `8`; equity avg `-0.3989` n `166`; fx avg `0.0495` n `6`; index avg `0.0054` n `27`; metal avg `-0.3886` n `20`; unknown avg `162.5951` n `1248`
- 24h: commodity avg `-1.2643` n `13`; crypto_alt avg `0.5157` n `239`; crypto_major avg `0.1294` n `8`; equity avg `4.6834` n `166`; fx avg `-0.2794` n `6`; index avg `0.6565` n `27`; metal avg `0.0353` n `20`; unknown avg `318.1517` n `1038`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
