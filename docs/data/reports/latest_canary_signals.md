# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T12:52:28.422139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0435` n `230`; crypto_major avg `0.0561` n `8`; equity avg `-0.0196` n `102`; fx avg `0.028` n `6`; index avg `-0.021` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0046` n `782`
- 1h: commodity avg `0.0604` n `12`; crypto_alt avg `0.1266` n `230`; crypto_major avg `0.1204` n `8`; equity avg `-0.1067` n `102`; fx avg `0.0315` n `6`; index avg `-0.0147` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.0386` n `781`
- 4h: commodity avg `0.0527` n `12`; crypto_alt avg `-0.1171` n `230`; crypto_major avg `-0.1549` n `8`; equity avg `-0.1012` n `102`; fx avg `-0.058` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0918` n `781`
- 24h: commodity avg `0.4326` n `12`; crypto_alt avg `0.3645` n `230`; crypto_major avg `-1.2659` n `8`; equity avg `-2.2551` n `102`; fx avg `-0.1573` n `6`; index avg `-0.231` n `25`; metal avg `-0.0026` n `20`; unknown avg `4.4406` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
