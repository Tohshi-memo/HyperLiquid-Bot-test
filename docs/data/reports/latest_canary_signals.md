# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T19:16:19.033160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `-0.0178` n `8`; equity avg `0.0164` n `88`; fx avg `-0.0006` n `6`; index avg `-0.012` n `23`; metal avg `0.0008` n `20`; unknown avg `-0.0166` n `764`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `0.149` n `228`; crypto_major avg `0.0365` n `8`; equity avg `0.0471` n `88`; fx avg `0.0` n `6`; index avg `-0.0258` n `23`; metal avg `-0.005` n `20`; unknown avg `-0.1589` n `764`
- 4h: commodity avg `-0.1582` n `12`; crypto_alt avg `-0.4886` n `228`; crypto_major avg `-0.9084` n `8`; equity avg `-0.1099` n `88`; fx avg `0.0031` n `6`; index avg `-0.0571` n `23`; metal avg `-0.0401` n `20`; unknown avg `0.0833` n `764`
- 24h: commodity avg `0.243` n `12`; crypto_alt avg `-0.1513` n `228`; crypto_major avg `-0.2478` n `8`; equity avg `0.6863` n `88`; fx avg `0.078` n `6`; index avg `-0.0669` n `23`; metal avg `0.1174` n `20`; unknown avg `-0.1395` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
