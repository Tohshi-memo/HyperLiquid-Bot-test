# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T04:07:19.046719+00:00`
- Correlation status: `ready`
- Asset price records: `516`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2349` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.2326` n `228`; crypto_major avg `-0.1329` n `8`; equity avg `-0.0009` n `65`; fx avg `0.0032` n `4`; index avg `-0.0105` n `23`; metal avg `-0.0486` n `18`; unknown avg `-0.1246` n `358`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.3472` n `228`; crypto_major avg `-0.1958` n `8`; equity avg `0.0915` n `65`; fx avg `0.0454` n `4`; index avg `0.0065` n `23`; metal avg `-0.1836` n `18`; unknown avg `-0.127` n `358`
- 4h: commodity avg `-0.2599` n `12`; crypto_alt avg `-1.2412` n `228`; crypto_major avg `-1.1467` n `8`; equity avg `0.0914` n `65`; fx avg `0.0851` n `4`; index avg `0.0882` n `23`; metal avg `0.1396` n `18`; unknown avg `-0.3837` n `356`
- 24h: commodity avg `-1.7785` n `7`; crypto_alt avg `-0.3492` n `223`; crypto_major avg `-1.6351` n `7`; equity avg `1.2181` n `47`; fx avg `-0.2087` n `4`; index avg `1.154` n `6`; metal avg `1.4989` n `7`; unknown avg `1.435` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `512`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `512`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `512`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `512`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `508`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `508`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0734`, n `508`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `508`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0688`, n `512`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0678`, n `508`, weak_sample_signal
