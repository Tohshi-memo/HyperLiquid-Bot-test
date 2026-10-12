# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T10:37:28.768562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `0.0605` n `235`; crypto_major avg `0.0936` n `8`; equity avg `-0.0129` n `151`; fx avg `0.0029` n `6`; index avg `0.0071` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.0056` n `1133`
- 1h: commodity avg `-0.067` n `13`; crypto_alt avg `-0.0934` n `235`; crypto_major avg `0.1023` n `8`; equity avg `-0.0012` n `151`; fx avg `-0.0058` n `6`; index avg `-0.0028` n `26`; metal avg `0.0762` n `20`; unknown avg `-0.0361` n `1131`
- 4h: commodity avg `0.1767` n `13`; crypto_alt avg `-0.8309` n `235`; crypto_major avg `-0.4859` n `8`; equity avg `-0.5073` n `151`; fx avg `-0.0466` n `6`; index avg `-0.0671` n `26`; metal avg `0.0168` n `20`; unknown avg `0.1438` n `997`
- 24h: commodity avg `-0.0861` n `13`; crypto_alt avg `2.0993` n `235`; crypto_major avg `1.4549` n `8`; equity avg `-1.0971` n `151`; fx avg `-0.1037` n `6`; index avg `-0.1415` n `26`; metal avg `0.0626` n `20`; unknown avg `-0.0115` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2222`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
