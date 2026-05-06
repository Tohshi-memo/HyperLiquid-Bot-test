# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T20:50:05.781285+00:00`
- Correlation status: `ready`
- Asset price records: `487`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.1361` n `228`; crypto_major avg `-0.1372` n `8`; equity avg `-0.1937` n `65`; fx avg `0.0072` n `4`; index avg `-0.0562` n `23`; metal avg `-0.0825` n `18`; unknown avg `-0.0611` n `356`
- 1h: commodity avg `0.3395` n `12`; crypto_alt avg `-0.0497` n `228`; crypto_major avg `-0.2664` n `8`; equity avg `-0.0676` n `65`; fx avg `0.0057` n `4`; index avg `-0.0454` n `23`; metal avg `-0.1001` n `18`; unknown avg `0.0561` n `356`
- 4h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.4959` n `228`; crypto_major avg `-0.5153` n `8`; equity avg `0.648` n `65`; fx avg `-0.0642` n `4`; index avg `0.3688` n `23`; metal avg `0.1469` n `18`; unknown avg `-0.3201` n `356`
- 24h: commodity avg `-2.3265` n `7`; crypto_alt avg `1.5277` n `223`; crypto_major avg `-0.1084` n `7`; equity avg `2.7254` n `47`; fx avg `-0.4804` n `4`; index avg `1.5836` n `6`; metal avg `3.4139` n `7`; unknown avg `3.7012` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1819`, n `479`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1699`, n `479`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1504`, n `479`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1406`, n `479`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.134`, n `483`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `483`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `479`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `479`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `483`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `483`, weak_sample_signal
