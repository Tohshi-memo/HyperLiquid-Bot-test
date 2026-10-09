# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T14:07:29.204957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0278` n `13`; crypto_alt avg `-0.0441` n `235`; crypto_major avg `-0.0149` n `8`; equity avg `0.1683` n `150`; fx avg `0.0254` n `6`; index avg `0.0193` n `26`; metal avg `-0.0567` n `20`; unknown avg `0.7052` n `1070`
- 1h: commodity avg `0.2585` n `13`; crypto_alt avg `-0.4926` n `235`; crypto_major avg `-0.5007` n `8`; equity avg `-0.6176` n `150`; fx avg `0.0162` n `6`; index avg `-0.0675` n `26`; metal avg `0.1262` n `20`; unknown avg `1.659` n `1028`
- 4h: commodity avg `0.3559` n `13`; crypto_alt avg `-0.8114` n `235`; crypto_major avg `-0.5418` n `8`; equity avg `-0.5939` n `150`; fx avg `-0.0335` n `6`; index avg `-0.0813` n `26`; metal avg `0.0782` n `20`; unknown avg `2.1929` n `1022`
- 24h: commodity avg `-0.1768` n `13`; crypto_alt avg `-1.7663` n `235`; crypto_major avg `-1.3473` n `8`; equity avg `-0.6394` n `150`; fx avg `0.0159` n `6`; index avg `-0.044` n `26`; metal avg `0.6249` n `20`; unknown avg `1.8373` n `933`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
