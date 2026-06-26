# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T21:52:31.292795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0387` n `12`; crypto_alt avg `0.004` n `228`; crypto_major avg `0.0612` n `8`; equity avg `0.0593` n `88`; fx avg `-0.0252` n `6`; index avg `0.0054` n `23`; metal avg `0.0222` n `20`; unknown avg `1.0129` n `764`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `0.1344` n `228`; crypto_major avg `0.2409` n `8`; equity avg `0.1228` n `88`; fx avg `0.0894` n `6`; index avg `0.0284` n `23`; metal avg `-0.015` n `20`; unknown avg `-0.0846` n `764`
- 4h: commodity avg `0.1465` n `12`; crypto_alt avg `-0.3716` n `228`; crypto_major avg `-0.2978` n `8`; equity avg `-0.1863` n `87`; fx avg `0.0903` n `6`; index avg `-0.1625` n `23`; metal avg `-0.0162` n `20`; unknown avg `-0.4108` n `764`
- 24h: commodity avg `-0.2633` n `12`; crypto_alt avg `1.4372` n `228`; crypto_major avg `1.2591` n `8`; equity avg `-0.4758` n `87`; fx avg `0.0152` n `6`; index avg `-0.3621` n `23`; metal avg `0.6248` n `20`; unknown avg `-0.6898` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
