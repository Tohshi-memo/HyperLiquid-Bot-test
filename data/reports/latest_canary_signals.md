# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T23:07:26.854376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0489` n `12`; crypto_alt avg `0.0303` n `230`; crypto_major avg `0.0354` n `8`; equity avg `0.0283` n `102`; fx avg `-0.0143` n `6`; index avg `-0.0211` n `25`; metal avg `-0.0031` n `20`; unknown avg `1.1156` n `781`
- 1h: commodity avg `0.1404` n `12`; crypto_alt avg `0.0394` n `230`; crypto_major avg `0.0329` n `8`; equity avg `-0.0074` n `102`; fx avg `0.0092` n `6`; index avg `-0.0045` n `25`; metal avg `0.0087` n `20`; unknown avg `1.0359` n `781`
- 4h: commodity avg `0.6622` n `12`; crypto_alt avg `-0.2838` n `230`; crypto_major avg `-0.2851` n `8`; equity avg `-0.8568` n `102`; fx avg `-0.106` n `6`; index avg `-0.1198` n `25`; metal avg `-0.0752` n `20`; unknown avg `2.0708` n `780`
- 24h: commodity avg `0.8251` n `12`; crypto_alt avg `-0.7666` n `230`; crypto_major avg `-2.4571` n `8`; equity avg `-1.6865` n `102`; fx avg `0.1079` n `6`; index avg `-0.0022` n `25`; metal avg `-0.4447` n `20`; unknown avg `2.5347` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
