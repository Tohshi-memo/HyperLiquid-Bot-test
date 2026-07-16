# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T19:22:30.659668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `-0.0395` n `8`; equity avg `-0.0105` n `94`; fx avg `-0.0037` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.0851` n `768`
- 1h: commodity avg `0.1016` n `12`; crypto_alt avg `-0.2667` n `230`; crypto_major avg `-0.1841` n `8`; equity avg `-0.4683` n `94`; fx avg `0.0066` n `6`; index avg `-0.1122` n `25`; metal avg `-0.0799` n `20`; unknown avg `-0.2136` n `768`
- 4h: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.4951` n `230`; crypto_major avg `-1.0427` n `8`; equity avg `-1.001` n `94`; fx avg `-0.0294` n `6`; index avg `-0.2134` n `25`; metal avg `-0.2981` n `20`; unknown avg `-0.2733` n `768`
- 24h: commodity avg `-0.2927` n `12`; crypto_alt avg `-0.8808` n `230`; crypto_major avg `-1.9143` n `8`; equity avg `-3.4551` n `94`; fx avg `-0.1577` n `6`; index avg `-0.517` n `25`; metal avg `-0.8209` n `20`; unknown avg `-0.3784` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
