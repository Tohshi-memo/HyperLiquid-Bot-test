# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T12:52:27.749395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0663` n `12`; crypto_alt avg `0.0123` n `230`; crypto_major avg `-0.1365` n `8`; equity avg `-0.1025` n `109`; fx avg `-0.0115` n `6`; index avg `-0.0029` n `25`; metal avg `-0.1137` n `20`; unknown avg `0.0028` n `781`
- 1h: commodity avg `0.1432` n `12`; crypto_alt avg `-0.054` n `230`; crypto_major avg `-0.265` n `8`; equity avg `-0.2989` n `109`; fx avg `-0.0006` n `6`; index avg `-0.0051` n `25`; metal avg `-0.1285` n `20`; unknown avg `-0.0037` n `781`
- 4h: commodity avg `0.2714` n `12`; crypto_alt avg `-0.2686` n `230`; crypto_major avg `-0.8569` n `8`; equity avg `-0.4542` n `109`; fx avg `-0.0095` n `6`; index avg `-0.0694` n `25`; metal avg `-0.1849` n `20`; unknown avg `108.1687` n `781`
- 24h: commodity avg `-0.0462` n `12`; crypto_alt avg `0.0933` n `230`; crypto_major avg `-0.89` n `8`; equity avg `-2.0016` n `109`; fx avg `-0.0019` n `6`; index avg `-0.4269` n `25`; metal avg `0.2692` n `20`; unknown avg `113.0933` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
