# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T19:07:28.851710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `0.1576` n `228`; crypto_major avg `0.236` n `8`; equity avg `0.2201` n `88`; fx avg `0.003` n `6`; index avg `-0.0279` n `23`; metal avg `-0.0284` n `20`; unknown avg `-0.266` n `764`
- 1h: commodity avg `-0.142` n `12`; crypto_alt avg `-0.2642` n `228`; crypto_major avg `-0.369` n `8`; equity avg `-0.3181` n `88`; fx avg `0.0023` n `6`; index avg `-0.1207` n `23`; metal avg `-0.0975` n `20`; unknown avg `-0.3958` n `764`
- 4h: commodity avg `-0.0475` n `12`; crypto_alt avg `1.1921` n `228`; crypto_major avg `0.9082` n `8`; equity avg `0.3646` n `87`; fx avg `0.0027` n `6`; index avg `-0.0032` n `23`; metal avg `-0.0755` n `20`; unknown avg `-0.321` n `764`
- 24h: commodity avg `-0.6148` n `12`; crypto_alt avg `2.7216` n `228`; crypto_major avg `2.5098` n `8`; equity avg `-0.4685` n `87`; fx avg `-0.0712` n `6`; index avg `-0.3097` n `23`; metal avg `0.4589` n `20`; unknown avg `0.0945` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
