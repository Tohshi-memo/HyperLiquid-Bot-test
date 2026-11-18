# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T18:22:28.953880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0274` n `13`; crypto_alt avg `0.2052` n `239`; crypto_major avg `0.1935` n `8`; equity avg `0.1331` n `164`; fx avg `0.0047` n `6`; index avg `0.0187` n `27`; metal avg `-0.0134` n `20`; unknown avg `0.5141` n `1263`
- 1h: commodity avg `0.1383` n `13`; crypto_alt avg `0.0251` n `239`; crypto_major avg `0.2783` n `8`; equity avg `-0.0121` n `164`; fx avg `-0.0079` n `6`; index avg `-0.0117` n `27`; metal avg `-0.0052` n `20`; unknown avg `0.1891` n `1263`
- 4h: commodity avg `-0.313` n `13`; crypto_alt avg `-0.7226` n `239`; crypto_major avg `-0.8479` n `8`; equity avg `-0.9283` n `164`; fx avg `-0.0087` n `6`; index avg `-0.0513` n `27`; metal avg `-0.2247` n `20`; unknown avg `4.0868` n `1257`
- 24h: commodity avg `-0.5161` n `13`; crypto_alt avg `0.6108` n `239`; crypto_major avg `0.0069` n `8`; equity avg `0.5209` n `164`; fx avg `-0.1943` n `6`; index avg `0.0695` n `27`; metal avg `-1.174` n `20`; unknown avg `0.107` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
