# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T06:37:32.759791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `12`; crypto_alt avg `-0.0032` n `233`; crypto_major avg `-0.0948` n `8`; equity avg `-0.1044` n `136`; fx avg `-0.0068` n `6`; index avg `-0.0204` n `27`; metal avg `-0.044` n `20`; unknown avg `0.6199` n `906`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.1384` n `233`; crypto_major avg `0.1254` n `8`; equity avg `0.0365` n `136`; fx avg `0.0079` n `6`; index avg `0.0029` n `27`; metal avg `-0.0331` n `20`; unknown avg `0.455` n `884`
- 4h: commodity avg `0.0739` n `12`; crypto_alt avg `-0.7193` n `233`; crypto_major avg `-0.7885` n `8`; equity avg `-0.7299` n `136`; fx avg `0.0392` n `6`; index avg `-0.1361` n `27`; metal avg `-0.1126` n `20`; unknown avg `2.3968` n `868`
- 24h: commodity avg `0.147` n `12`; crypto_alt avg `-1.1821` n `233`; crypto_major avg `-0.2026` n `8`; equity avg `-0.4642` n `136`; fx avg `0.1434` n `6`; index avg `-0.0797` n `27`; metal avg `-0.3573` n `20`; unknown avg `4.399` n `796`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
