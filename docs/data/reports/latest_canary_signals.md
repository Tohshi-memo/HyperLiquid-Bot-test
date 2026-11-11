# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T10:52:26.308791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0546` n `13`; crypto_alt avg `-0.0597` n `239`; crypto_major avg `-0.1026` n `8`; equity avg `0.1627` n `161`; fx avg `0.0331` n `6`; index avg `0.0301` n `27`; metal avg `0.0162` n `20`; unknown avg `-0.0929` n `1261`
- 1h: commodity avg `0.1371` n `13`; crypto_alt avg `0.497` n `239`; crypto_major avg `0.4492` n `8`; equity avg `0.3806` n `161`; fx avg `0.0806` n `6`; index avg `0.0183` n `27`; metal avg `0.0176` n `20`; unknown avg `19.3281` n `1253`
- 4h: commodity avg `0.2561` n `13`; crypto_alt avg `0.6685` n `239`; crypto_major avg `0.7849` n `8`; equity avg `0.7768` n `161`; fx avg `0.0174` n `6`; index avg `-0.0095` n `27`; metal avg `0.1264` n `20`; unknown avg `0.0956` n `1223`
- 24h: commodity avg `0.7974` n `13`; crypto_alt avg `-0.3657` n `239`; crypto_major avg `-1.0121` n `8`; equity avg `2.869` n `161`; fx avg `-0.1882` n `6`; index avg `0.2759` n `27`; metal avg `0.3051` n `20`; unknown avg `1.3073` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
