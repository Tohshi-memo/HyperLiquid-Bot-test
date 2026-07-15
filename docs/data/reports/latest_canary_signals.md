# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T07:37:36.167147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.0952` n `230`; crypto_major avg `-0.1118` n `8`; equity avg `-0.0717` n `93`; fx avg `-0.0013` n `6`; index avg `-0.0254` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.0113` n `767`
- 1h: commodity avg `0.1198` n `12`; crypto_alt avg `-0.5941` n `230`; crypto_major avg `-0.6853` n `8`; equity avg `-0.1404` n `93`; fx avg `0.0245` n `6`; index avg `-0.0524` n `25`; metal avg `-0.0628` n `20`; unknown avg `0.0305` n `767`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.3464` n `230`; crypto_major avg `-0.1693` n `8`; equity avg `-0.1747` n `93`; fx avg `-0.004` n `6`; index avg `-0.0725` n `25`; metal avg `-0.1254` n `20`; unknown avg `0.0616` n `749`
- 24h: commodity avg `-0.0666` n `12`; crypto_alt avg `1.2186` n `230`; crypto_major avg `3.0105` n `8`; equity avg `1.5006` n `92`; fx avg `0.0795` n `6`; index avg `0.4124` n `25`; metal avg `0.1494` n `20`; unknown avg `0.2177` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
