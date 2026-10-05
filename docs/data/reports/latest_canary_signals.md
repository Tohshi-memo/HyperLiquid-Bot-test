# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T05:37:27.000085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0605` n `13`; crypto_alt avg `0.2846` n `235`; crypto_major avg `0.2366` n `8`; equity avg `-0.0242` n `144`; fx avg `-0.0049` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0186` n `20`; unknown avg `4.0469` n `1079`
- 1h: commodity avg `0.0096` n `13`; crypto_alt avg `0.5127` n `235`; crypto_major avg `0.1521` n `8`; equity avg `-0.0187` n `144`; fx avg `0.0059` n `6`; index avg `-0.0143` n `26`; metal avg `0.0335` n `20`; unknown avg `2.0704` n `1075`
- 4h: commodity avg `0.0187` n `13`; crypto_alt avg `-0.3` n `235`; crypto_major avg `-0.5474` n `8`; equity avg `-0.4452` n `144`; fx avg `-0.0093` n `6`; index avg `-0.1277` n `26`; metal avg `-0.1351` n `20`; unknown avg `3.8195` n `982`
- 24h: commodity avg `-0.2893` n `13`; crypto_alt avg `0.1889` n `235`; crypto_major avg `0.795` n `8`; equity avg `0.1692` n `144`; fx avg `-0.0572` n `6`; index avg `-0.0676` n `26`; metal avg `0.0515` n `20`; unknown avg `0.1085` n `904`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
