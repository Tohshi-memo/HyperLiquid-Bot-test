# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T20:22:26.134189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `13`; crypto_alt avg `0.2037` n `235`; crypto_major avg `0.099` n `8`; equity avg `0.0169` n `150`; fx avg `-0.005` n `6`; index avg `0.0049` n `26`; metal avg `-0.0192` n `20`; unknown avg `8.6215` n `1028`
- 1h: commodity avg `0.0415` n `13`; crypto_alt avg `0.2872` n `235`; crypto_major avg `0.3158` n `8`; equity avg `-0.0353` n `150`; fx avg `-0.0085` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0536` n `20`; unknown avg `9.015` n `1012`
- 4h: commodity avg `0.3912` n `13`; crypto_alt avg `-0.3296` n `235`; crypto_major avg `-0.2372` n `8`; equity avg `-0.1936` n `150`; fx avg `0.0052` n `6`; index avg `-0.0869` n `26`; metal avg `0.0383` n `20`; unknown avg `8.7858` n `1012`
- 24h: commodity avg `0.2883` n `13`; crypto_alt avg `-0.8412` n `235`; crypto_major avg `-0.6383` n `8`; equity avg `0.3502` n `149`; fx avg `0.1009` n `6`; index avg `-0.0206` n `26`; metal avg `0.0522` n `20`; unknown avg `868.4974` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
