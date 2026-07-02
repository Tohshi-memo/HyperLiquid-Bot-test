# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T07:37:30.636682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1009` n `12`; crypto_alt avg `0.056` n `228`; crypto_major avg `0.0296` n `8`; equity avg `0.1584` n `88`; fx avg `-0.0059` n `6`; index avg `0.0281` n `25`; metal avg `0.0356` n `20`; unknown avg `0.0115` n `763`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.1499` n `228`; crypto_major avg `-0.525` n `8`; equity avg `-0.4021` n `88`; fx avg `-0.0487` n `6`; index avg `-0.0682` n `25`; metal avg `-0.1424` n `20`; unknown avg `-0.0107` n `763`
- 4h: commodity avg `0.0465` n `12`; crypto_alt avg `-0.2184` n `228`; crypto_major avg `-0.5393` n `8`; equity avg `-1.3373` n `88`; fx avg `-0.0478` n `6`; index avg `-0.2939` n `25`; metal avg `-0.1158` n `20`; unknown avg `0.0302` n `739`
- 24h: commodity avg `-0.5678` n `12`; crypto_alt avg `1.9817` n `228`; crypto_major avg `1.3043` n `8`; equity avg `-2.3094` n `88`; fx avg `-0.0467` n `6`; index avg `-0.57` n `25`; metal avg `1.1165` n `20`; unknown avg `25.1088` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
