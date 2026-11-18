# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T22:52:27.925271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.4289` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0297` n `13`; crypto_alt avg `-0.5453` n `239`; crypto_major avg `-0.6331` n `8`; equity avg `-0.0642` n `164`; fx avg `-0.0006` n `6`; index avg `0.0036` n `27`; metal avg `-0.0179` n `20`; unknown avg `5.9281` n `1265`
- 1h: commodity avg `-0.0643` n `13`; crypto_alt avg `-0.7448` n `239`; crypto_major avg `-0.5057` n `8`; equity avg `-0.1207` n `164`; fx avg `0.0093` n `6`; index avg `-0.0074` n `27`; metal avg `-0.012` n `20`; unknown avg `0.573` n `1257`
- 4h: commodity avg `0.0025` n `13`; crypto_alt avg `-1.3315` n `239`; crypto_major avg `-1.478` n `8`; equity avg `-0.6427` n `164`; fx avg `-0.0037` n `6`; index avg `-0.0491` n `27`; metal avg `-0.1135` n `20`; unknown avg `-0.3323` n `1219`
- 24h: commodity avg `-0.2482` n `13`; crypto_alt avg `-2.0401` n `239`; crypto_major avg `-2.6757` n `8`; equity avg `-2.4074` n `164`; fx avg `-0.1686` n `6`; index avg `-0.1985` n `27`; metal avg `-1.2037` n `20`; unknown avg `50.8735` n `1126`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
