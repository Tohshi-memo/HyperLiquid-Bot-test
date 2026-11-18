# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T12:07:47.012151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `13`; crypto_alt avg `-0.1271` n `239`; crypto_major avg `-0.0559` n `8`; equity avg `-0.1261` n `163`; fx avg `-0.0009` n `6`; index avg `-0.0111` n `27`; metal avg `0.0877` n `20`; unknown avg `-0.0198` n `1254`
- 1h: commodity avg `0.0785` n `13`; crypto_alt avg `0.1333` n `239`; crypto_major avg `-0.036` n `8`; equity avg `-0.2061` n `163`; fx avg `-0.0079` n `6`; index avg `-0.0407` n `27`; metal avg `0.0627` n `20`; unknown avg `0.0425` n `1258`
- 4h: commodity avg `0.2352` n `13`; crypto_alt avg `-0.1842` n `239`; crypto_major avg `-0.7651` n `8`; equity avg `-0.3095` n `163`; fx avg `-0.0041` n `6`; index avg `-0.0267` n `27`; metal avg `-0.0201` n `20`; unknown avg `134.0307` n `1198`
- 24h: commodity avg `-0.06` n `13`; crypto_alt avg `-0.0466` n `239`; crypto_major avg `-0.0157` n `8`; equity avg `-0.1408` n `163`; fx avg `-0.1141` n `6`; index avg `-0.009` n `27`; metal avg `-1.0768` n `20`; unknown avg `5.7183` n `1099`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
