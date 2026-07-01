# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T00:07:25.654686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.0881` n `228`; crypto_major avg `0.1375` n `8`; equity avg `-0.0258` n `88`; fx avg `0.0363` n `6`; index avg `0.0215` n `23`; metal avg `-0.0279` n `20`; unknown avg `0.1061` n `765`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.1104` n `228`; crypto_major avg `0.2772` n `8`; equity avg `0.06` n `88`; fx avg `0.0474` n `6`; index avg `0.0153` n `23`; metal avg `-0.1705` n `20`; unknown avg `-0.5253` n `765`
- 4h: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.3482` n `228`; crypto_major avg `-0.301` n `8`; equity avg `0.165` n `88`; fx avg `0.0206` n `6`; index avg `-0.0147` n `23`; metal avg `-0.2724` n `20`; unknown avg `-0.7517` n `765`
- 24h: commodity avg `0.1581` n `12`; crypto_alt avg `-2.0922` n `228`; crypto_major avg `-1.8518` n `8`; equity avg `1.2455` n `88`; fx avg `0.1162` n `6`; index avg `0.235` n `23`; metal avg `-0.0753` n `20`; unknown avg `7.3499` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
