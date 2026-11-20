# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T07:53:02.701074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.2363` n `239`; crypto_major avg `0.5167` n `8`; equity avg `0.4666` n `165`; fx avg `0.0158` n `6`; index avg `0.0657` n `27`; metal avg `0.2611` n `20`; unknown avg `1.661` n `1262`
- 1h: commodity avg `-0.0537` n `13`; crypto_alt avg `0.0425` n `239`; crypto_major avg `0.013` n `8`; equity avg `0.2152` n `165`; fx avg `-0.0126` n `6`; index avg `0.0547` n `27`; metal avg `0.1037` n `20`; unknown avg `0.6822` n `1258`
- 4h: commodity avg `-0.225` n `13`; crypto_alt avg `0.0914` n `239`; crypto_major avg `-0.1098` n `8`; equity avg `-0.7355` n `165`; fx avg `-0.0149` n `6`; index avg `-0.0138` n `27`; metal avg `0.2093` n `20`; unknown avg `-0.1902` n `1226`
- 24h: commodity avg `-0.1775` n `13`; crypto_alt avg `-2.9787` n `239`; crypto_major avg `-2.3717` n `8`; equity avg `-6.7498` n `165`; fx avg `-0.0241` n `6`; index avg `-0.6091` n `27`; metal avg `-1.3613` n `20`; unknown avg `62.087` n `1179`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
