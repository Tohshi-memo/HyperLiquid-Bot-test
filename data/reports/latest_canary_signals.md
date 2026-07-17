# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T01:22:25.731333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0634` n `12`; crypto_alt avg `-0.1968` n `230`; crypto_major avg `-0.2261` n `8`; equity avg `-0.2325` n `94`; fx avg `0.0089` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0219` n `20`; unknown avg `-0.0935` n `768`
- 1h: commodity avg `0.1306` n `12`; crypto_alt avg `0.1289` n `230`; crypto_major avg `0.1348` n `8`; equity avg `-0.0872` n `94`; fx avg `-0.0282` n `6`; index avg `0.0014` n `25`; metal avg `0.0349` n `20`; unknown avg `-0.1378` n `768`
- 4h: commodity avg `0.114` n `12`; crypto_alt avg `-0.8091` n `230`; crypto_major avg `-0.6902` n `8`; equity avg `-1.0526` n `94`; fx avg `-0.0077` n `6`; index avg `-0.1581` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.431` n `768`
- 24h: commodity avg `-0.0182` n `12`; crypto_alt avg `-1.2316` n `230`; crypto_major avg `-2.0563` n `8`; equity avg `-4.0736` n `94`; fx avg `-0.177` n `6`; index avg `-0.4599` n `25`; metal avg `-0.6115` n `20`; unknown avg `-0.588` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
