# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T00:07:29.066550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `0.0785` n `235`; crypto_major avg `-0.0066` n `8`; equity avg `0.0569` n `150`; fx avg `-0.0442` n `6`; index avg `-0.0066` n `26`; metal avg `0.0237` n `20`; unknown avg `0.0622` n `1126`
- 1h: commodity avg `-0.4041` n `13`; crypto_alt avg `0.251` n `235`; crypto_major avg `0.0841` n `8`; equity avg `0.0929` n `150`; fx avg `-0.0271` n `6`; index avg `0.0084` n `26`; metal avg `0.0887` n `20`; unknown avg `0.1124` n `1126`
- 4h: commodity avg `-0.3435` n `13`; crypto_alt avg `0.2686` n `235`; crypto_major avg `0.1138` n `8`; equity avg `0.173` n `150`; fx avg `-0.0521` n `6`; index avg `0.0104` n `26`; metal avg `0.0187` n `20`; unknown avg `-0.0774` n `1098`
- 24h: commodity avg `-0.2552` n `13`; crypto_alt avg `2.2765` n `235`; crypto_major avg `0.8464` n `8`; equity avg `0.4431` n `150`; fx avg `-0.0287` n `6`; index avg `0.0443` n `26`; metal avg `0.0941` n `20`; unknown avg `0.5823` n `957`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
