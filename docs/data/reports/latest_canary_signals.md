# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T20:07:33.671724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.031` n `12`; crypto_alt avg `0.0581` n `228`; crypto_major avg `-0.0447` n `8`; equity avg `-0.0425` n `88`; fx avg `0.0028` n `6`; index avg `-0.0733` n `23`; metal avg `-0.0796` n `20`; unknown avg `-0.0054` n `764`
- 1h: commodity avg `0.0799` n `12`; crypto_alt avg `-0.0158` n `228`; crypto_major avg `0.0534` n `8`; equity avg `0.0337` n `88`; fx avg `-0.008` n `6`; index avg `-0.0931` n `23`; metal avg `-0.0356` n `20`; unknown avg `-0.0771` n `764`
- 4h: commodity avg `-0.0655` n `12`; crypto_alt avg `0.4027` n `228`; crypto_major avg `0.1947` n `8`; equity avg `-0.1493` n `87`; fx avg `-0.017` n `6`; index avg `-0.1734` n `23`; metal avg `-0.2143` n `20`; unknown avg `-0.3656` n `764`
- 24h: commodity avg `-0.5497` n `12`; crypto_alt avg `2.7609` n `228`; crypto_major avg `2.3194` n `8`; equity avg `-0.6682` n `87`; fx avg `-0.0806` n `6`; index avg `-0.4236` n `23`; metal avg `0.4991` n `20`; unknown avg `-0.1693` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
