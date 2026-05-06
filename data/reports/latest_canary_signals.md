# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T22:22:15.007921+00:00`
- Correlation status: `ready`
- Asset price records: `493`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.8` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.2584` n `228`; crypto_major avg `-0.1564` n `8`; equity avg `0.0954` n `65`; fx avg `0.0017` n `4`; index avg `0.0045` n `23`; metal avg `0.1095` n `18`; unknown avg `0.981` n `356`
- 1h: commodity avg `-0.0793` n `12`; crypto_alt avg `-0.0962` n `228`; crypto_major avg `-0.1722` n `8`; equity avg `-0.1012` n `65`; fx avg `0.0027` n `4`; index avg `-0.0015` n `23`; metal avg `0.0168` n `18`; unknown avg `0.9877` n `356`
- 4h: commodity avg `0.3552` n `12`; crypto_alt avg `0.1247` n `228`; crypto_major avg `-0.1291` n `8`; equity avg `0.0411` n `65`; fx avg `-0.0176` n `4`; index avg `0.1016` n `23`; metal avg `0.202` n `18`; unknown avg `1.1442` n `356`
- 24h: commodity avg `-2.3042` n `7`; crypto_alt avg `1.7634` n `223`; crypto_major avg `-0.2057` n `7`; equity avg `2.0398` n `47`; fx avg `-0.6063` n `4`; index avg `1.461` n `6`; metal avg `3.6168` n `7`; unknown avg `4.2507` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1312`, n `489`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `489`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `485`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0839`, n `485`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0825`, n `485`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `485`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `489`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.072`, n `489`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0703`, n `485`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `485`, weak_sample_signal
