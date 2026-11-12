# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T06:22:31.713360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.1771` n `239`; crypto_major avg `0.131` n `8`; equity avg `0.2872` n `161`; fx avg `0.0068` n `6`; index avg `0.0318` n `27`; metal avg `0.04` n `20`; unknown avg `41.0502` n `1260`
- 1h: commodity avg `0.1294` n `13`; crypto_alt avg `0.0781` n `239`; crypto_major avg `0.1634` n `8`; equity avg `0.1996` n `161`; fx avg `0.0125` n `6`; index avg `0.0394` n `27`; metal avg `0.0722` n `20`; unknown avg `44.0241` n `1226`
- 4h: commodity avg `0.0249` n `13`; crypto_alt avg `-0.5776` n `239`; crypto_major avg `-0.6278` n `8`; equity avg `-1.3023` n `161`; fx avg `-0.0872` n `6`; index avg `-0.106` n `27`; metal avg `-0.0687` n `20`; unknown avg `0.1685` n `1208`
- 24h: commodity avg `0.1764` n `13`; crypto_alt avg `-1.4015` n `239`; crypto_major avg `-0.7301` n `8`; equity avg `-0.5377` n `161`; fx avg `-0.1954` n `6`; index avg `-0.0617` n `27`; metal avg `-0.58` n `20`; unknown avg `0.4523` n `1127`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
