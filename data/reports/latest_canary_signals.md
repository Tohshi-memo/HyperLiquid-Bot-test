# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T21:22:25.739324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0428` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0773` n `12`; crypto_alt avg `-0.4876` n `228`; crypto_major avg `-0.4146` n `8`; equity avg `-0.2623` n `74`; fx avg `0.0525` n `6`; index avg `-0.0803` n `23`; metal avg `-0.014` n `18`; unknown avg `-0.1326` n `547`
- 1h: commodity avg `0.274` n `12`; crypto_alt avg `-0.1601` n `228`; crypto_major avg `-0.0592` n `8`; equity avg `-0.1907` n `74`; fx avg `0.0489` n `6`; index avg `0.0209` n `23`; metal avg `0.0503` n `18`; unknown avg `-0.0618` n `547`
- 4h: commodity avg `0.5316` n `12`; crypto_alt avg `0.1466` n `228`; crypto_major avg `0.1028` n `8`; equity avg `0.9149` n `74`; fx avg `-0.0241` n `6`; index avg `1.1456` n `23`; metal avg `0.0989` n `18`; unknown avg `0.122` n `547`
- 24h: commodity avg `-0.812` n `12`; crypto_alt avg `-2.2635` n `228`; crypto_major avg `-3.3679` n `8`; equity avg `-2.0401` n `74`; fx avg `0.0846` n `6`; index avg `-0.9405` n `23`; metal avg `-1.5226` n `18`; unknown avg `-1.2133` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
