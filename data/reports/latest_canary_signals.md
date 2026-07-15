# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T05:22:28.954363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1258` n `230`; crypto_major avg `-0.0798` n `8`; equity avg `-0.099` n `93`; fx avg `-0.0131` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0529` n `20`; unknown avg `-0.088` n `767`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.2383` n `230`; crypto_major avg `-0.1811` n `8`; equity avg `-0.3571` n `93`; fx avg `-0.0149` n `6`; index avg `-0.045` n `25`; metal avg `-0.0638` n `20`; unknown avg `-0.1443` n `767`
- 4h: commodity avg `0.0161` n `12`; crypto_alt avg `-0.3136` n `230`; crypto_major avg `0.1134` n `8`; equity avg `0.7624` n `93`; fx avg `0.037` n `6`; index avg `0.0902` n `25`; metal avg `-0.1831` n `20`; unknown avg `-0.3276` n `767`
- 24h: commodity avg `0.058` n `12`; crypto_alt avg `1.2984` n `230`; crypto_major avg `2.6946` n `8`; equity avg `1.7098` n `92`; fx avg `0.1101` n `6`; index avg `0.4823` n `25`; metal avg `0.2346` n `20`; unknown avg `0.3135` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
