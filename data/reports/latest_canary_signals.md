# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T03:52:17.461410+00:00`
- Correlation status: `ready`
- Asset price records: `515`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0757` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `0.0856` n `228`; crypto_major avg `0.033` n `8`; equity avg `0.0248` n `65`; fx avg `0.032` n `4`; index avg `0.003` n `23`; metal avg `-0.039` n `18`; unknown avg `0.0574` n `358`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.0759` n `228`; crypto_major avg `-0.1312` n `8`; equity avg `0.1597` n `65`; fx avg `0.0584` n `4`; index avg `0.0216` n `23`; metal avg `-0.0962` n `18`; unknown avg `-0.0214` n `358`
- 4h: commodity avg `-0.1221` n `12`; crypto_alt avg `-1.0616` n `228`; crypto_major avg `-0.9805` n `8`; equity avg `-0.0225` n `65`; fx avg `0.1322` n `4`; index avg `0.0952` n `23`; metal avg `0.0684` n `18`; unknown avg `-0.5038` n `356`
- 24h: commodity avg `-1.6798` n `7`; crypto_alt avg `-0.0289` n `223`; crypto_major avg `-1.4015` n `7`; equity avg `1.3476` n `47`; fx avg `-0.2167` n `4`; index avg `1.1812` n `6`; metal avg `1.6049` n `7`; unknown avg `1.76` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1272`, n `511`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `511`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `511`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `511`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `507`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `507`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0729`, n `507`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `507`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.069`, n `507`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `511`, weak_sample_signal
