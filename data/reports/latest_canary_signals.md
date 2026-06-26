# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T23:42:36.720059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0612` n `228`; crypto_major avg `0.1881` n `8`; equity avg `0.0339` n `88`; fx avg `-0.0558` n `6`; index avg `0.0133` n `23`; metal avg `-0.0009` n `20`; unknown avg `0.1081` n `764`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.3025` n `228`; crypto_major avg `0.3487` n `8`; equity avg `0.1308` n `88`; fx avg `-0.0184` n `6`; index avg `0.0211` n `23`; metal avg `0.0427` n `20`; unknown avg `0.1771` n `764`
- 4h: commodity avg `0.1926` n `12`; crypto_alt avg `-0.3486` n `228`; crypto_major avg `-0.2358` n `8`; equity avg `0.2762` n `88`; fx avg `0.0523` n `6`; index avg `-0.0268` n `23`; metal avg `0.1248` n `20`; unknown avg `-0.1681` n `748`
- 24h: commodity avg `-0.2475` n `12`; crypto_alt avg `1.286` n `228`; crypto_major avg `0.8861` n `8`; equity avg `-0.5041` n `87`; fx avg `0.0061` n `6`; index avg `-0.4007` n `23`; metal avg `0.7129` n `20`; unknown avg `0.2151` n `684`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
