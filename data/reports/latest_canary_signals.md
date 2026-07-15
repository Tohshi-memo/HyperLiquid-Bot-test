# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T18:52:25.828274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.88` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.1823` n `230`; crypto_major avg `-0.3068` n `8`; equity avg `-0.3947` n `94`; fx avg `-0.0078` n `6`; index avg `-0.0733` n `25`; metal avg `-0.0442` n `20`; unknown avg `0.0237` n `768`
- 1h: commodity avg `0.1279` n `12`; crypto_alt avg `-0.1185` n `230`; crypto_major avg `-0.1696` n `8`; equity avg `-0.223` n `94`; fx avg `-0.0071` n `6`; index avg `-0.0352` n `25`; metal avg `0.1679` n `20`; unknown avg `-0.0528` n `768`
- 4h: commodity avg `0.2359` n `12`; crypto_alt avg `-0.4043` n `230`; crypto_major avg `-0.6636` n `8`; equity avg `-0.2404` n `94`; fx avg `0.048` n `6`; index avg `0.0557` n `25`; metal avg `0.167` n `20`; unknown avg `0.0341` n `768`
- 24h: commodity avg `0.0648` n `12`; crypto_alt avg `0.5887` n `230`; crypto_major avg `0.912` n `8`; equity avg `-0.6015` n `93`; fx avg `0.2162` n `6`; index avg `-0.206` n `25`; metal avg `0.2078` n `20`; unknown avg `0.3135` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
