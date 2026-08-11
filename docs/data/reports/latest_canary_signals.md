# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T18:37:32.817279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `12`; crypto_alt avg `-0.0461` n `230`; crypto_major avg `-0.1192` n `8`; equity avg `-0.0995` n `113`; fx avg `0.0022` n `6`; index avg `-0.015` n `25`; metal avg `0.0441` n `20`; unknown avg `-0.0587` n `785`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.0084` n `230`; crypto_major avg `0.0042` n `8`; equity avg `-0.1352` n `113`; fx avg `0.0063` n `6`; index avg `-0.0425` n `25`; metal avg `-0.0369` n `20`; unknown avg `0.1223` n `785`
- 4h: commodity avg `0.1553` n `12`; crypto_alt avg `-1.0096` n `230`; crypto_major avg `-0.2037` n `8`; equity avg `-0.3889` n `113`; fx avg `0.0054` n `6`; index avg `-0.1299` n `25`; metal avg `-0.1771` n `20`; unknown avg `-0.1513` n `785`
- 24h: commodity avg `0.076` n `12`; crypto_alt avg `-1.8278` n `230`; crypto_major avg `-0.0447` n `8`; equity avg `0.0894` n `113`; fx avg `-0.0536` n `6`; index avg `0.039` n `25`; metal avg `-0.1517` n `20`; unknown avg `-0.2857` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
