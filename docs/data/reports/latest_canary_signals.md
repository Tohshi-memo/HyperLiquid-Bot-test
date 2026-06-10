# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T14:37:36.701486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0033` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1451` n `12`; crypto_alt avg `-0.1967` n `228`; crypto_major avg `-0.2647` n `8`; equity avg `0.0651` n `74`; fx avg `0.0022` n `6`; index avg `0.0141` n `23`; metal avg `-0.151` n `18`; unknown avg `-0.0849` n `548`
- 1h: commodity avg `0.3725` n `12`; crypto_alt avg `-0.5857` n `228`; crypto_major avg `-0.5049` n `8`; equity avg `0.635` n `74`; fx avg `-0.0441` n `6`; index avg `0.4984` n `23`; metal avg `-0.0387` n `18`; unknown avg `1.1097` n `547`
- 4h: commodity avg `0.9749` n `12`; crypto_alt avg `0.8706` n `228`; crypto_major avg `1.0573` n `8`; equity avg `2.0948` n `74`; fx avg `-0.0161` n `6`; index avg `0.9471` n `23`; metal avg `0.6623` n `18`; unknown avg `1.387` n `547`
- 24h: commodity avg `1.2266` n `12`; crypto_alt avg `0.6385` n `228`; crypto_major avg `-0.575` n `8`; equity avg `-0.9986` n `74`; fx avg `-0.0829` n `6`; index avg `-0.5054` n `23`; metal avg `-1.8563` n `18`; unknown avg `1.5019` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
