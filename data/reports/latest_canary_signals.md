# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T10:52:25.558900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0424` n `13`; crypto_alt avg `0.0916` n `235`; crypto_major avg `-0.0054` n `8`; equity avg `0.0573` n `151`; fx avg `-0.01` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0222` n `20`; unknown avg `0.0353` n `1133`
- 1h: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.1181` n `235`; crypto_major avg `0.0024` n `8`; equity avg `0.023` n `151`; fx avg `0.0027` n `6`; index avg `-0.0139` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.1085` n `1131`
- 4h: commodity avg `0.2361` n `13`; crypto_alt avg `-0.6635` n `235`; crypto_major avg `-0.5032` n `8`; equity avg `-0.395` n `151`; fx avg `-0.0544` n `6`; index avg `-0.0758` n `26`; metal avg `-0.0351` n `20`; unknown avg `0.1408` n `997`
- 24h: commodity avg `-0.0463` n `13`; crypto_alt avg `2.2045` n `235`; crypto_major avg `1.4021` n `8`; equity avg `-1.0334` n `151`; fx avg `-0.1151` n `6`; index avg `-0.1436` n `26`; metal avg `0.0439` n `20`; unknown avg `0.685` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2276`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
