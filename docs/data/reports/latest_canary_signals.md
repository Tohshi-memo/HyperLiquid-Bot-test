# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T12:07:29.626700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `0.0347` n `230`; crypto_major avg `-0.0254` n `8`; equity avg `-0.1131` n `93`; fx avg `0.0014` n `6`; index avg `-0.0226` n `25`; metal avg `-0.0264` n `20`; unknown avg `-0.0321` n `767`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.1568` n `230`; crypto_major avg `0.0526` n `8`; equity avg `-0.1287` n `93`; fx avg `0.0088` n `6`; index avg `-0.0396` n `25`; metal avg `0.0484` n `20`; unknown avg `0.0356` n `767`
- 4h: commodity avg `-0.1754` n `12`; crypto_alt avg `0.5024` n `230`; crypto_major avg `0.4696` n `8`; equity avg `-0.1211` n `93`; fx avg `-0.0055` n `6`; index avg `-0.045` n `25`; metal avg `-0.069` n `20`; unknown avg `0.0043` n `767`
- 24h: commodity avg `-0.0841` n `12`; crypto_alt avg `1.7924` n `230`; crypto_major avg `3.1632` n `8`; equity avg `1.3518` n `92`; fx avg `0.0159` n `6`; index avg `0.3226` n `25`; metal avg `0.2946` n `20`; unknown avg `0.2776` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
