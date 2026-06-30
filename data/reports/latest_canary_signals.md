# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T22:07:26.271655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `0.2687` n `228`; crypto_major avg `0.2452` n `8`; equity avg `0.0428` n `88`; fx avg `0.0068` n `6`; index avg `0.0097` n `23`; metal avg `0.0933` n `20`; unknown avg `0.1929` n `765`
- 1h: commodity avg `-0.0365` n `12`; crypto_alt avg `0.3754` n `228`; crypto_major avg `0.179` n `8`; equity avg `0.0813` n `88`; fx avg `0.0091` n `6`; index avg `0.0089` n `23`; metal avg `0.0994` n `20`; unknown avg `4.9805` n `765`
- 4h: commodity avg `-0.0667` n `12`; crypto_alt avg `0.0662` n `228`; crypto_major avg `0.3706` n `8`; equity avg `0.4596` n `88`; fx avg `-0.003` n `6`; index avg `-0.0324` n `23`; metal avg `-0.1971` n `20`; unknown avg `1.7177` n `763`
- 24h: commodity avg `0.1254` n `12`; crypto_alt avg `-2.2123` n `228`; crypto_major avg `-2.3549` n `8`; equity avg `1.2335` n `88`; fx avg `0.1145` n `6`; index avg `0.2564` n `23`; metal avg `0.0129` n `20`; unknown avg `12.0081` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
