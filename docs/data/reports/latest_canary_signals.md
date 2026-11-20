# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T02:07:29.244658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.5983` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0281` n `13`; crypto_alt avg `-0.6069` n `239`; crypto_major avg `-0.7646` n `8`; equity avg `-0.1893` n `165`; fx avg `0.0219` n `6`; index avg `-0.0208` n `27`; metal avg `-0.0796` n `20`; unknown avg `1.1131` n `1252`
- 1h: commodity avg `0.0352` n `13`; crypto_alt avg `-1.6463` n `239`; crypto_major avg `-1.7124` n `8`; equity avg `-1.1502` n `165`; fx avg `-0.0078` n `6`; index avg `-0.1141` n `27`; metal avg `-0.4517` n `20`; unknown avg `0.4756` n `1258`
- 4h: commodity avg `-0.0777` n `13`; crypto_alt avg `-0.9459` n `239`; crypto_major avg `-0.7492` n `8`; equity avg `-1.4572` n `165`; fx avg `0.0123` n `6`; index avg `-0.1523` n `27`; metal avg `-0.7141` n `20`; unknown avg `19.7719` n `1246`
- 24h: commodity avg `-0.1673` n `13`; crypto_alt avg `-2.3975` n `239`; crypto_major avg `-1.8324` n `8`; equity avg `-5.3958` n `165`; fx avg `0.0027` n `6`; index avg `-0.4174` n `27`; metal avg `-1.6844` n `20`; unknown avg `2.883` n `1166`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
