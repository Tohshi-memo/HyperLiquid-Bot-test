# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T15:52:34.688056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.131` n `12`; crypto_alt avg `-0.1489` n `230`; crypto_major avg `-0.2349` n `8`; equity avg `-0.257` n `108`; fx avg `0.0007` n `6`; index avg `-0.0501` n `25`; metal avg `-0.1447` n `20`; unknown avg `0.0393` n `782`
- 1h: commodity avg `0.1309` n `12`; crypto_alt avg `-0.0006` n `230`; crypto_major avg `0.0433` n `8`; equity avg `0.1134` n `108`; fx avg `-0.0224` n `6`; index avg `-0.0426` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0652` n `782`
- 4h: commodity avg `-0.1381` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `0.333` n `8`; equity avg `-0.2156` n `108`; fx avg `-0.0301` n `6`; index avg `-0.084` n `25`; metal avg `0.0209` n `20`; unknown avg `0.0566` n `782`
- 24h: commodity avg `0.0592` n `12`; crypto_alt avg `0.5258` n `230`; crypto_major avg `0.3275` n `8`; equity avg `0.0524` n `108`; fx avg `0.0214` n `6`; index avg `0.0814` n `25`; metal avg `0.6494` n `20`; unknown avg `0.7158` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
