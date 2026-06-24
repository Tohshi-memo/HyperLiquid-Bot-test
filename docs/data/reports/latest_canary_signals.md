# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T14:07:38.306478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.261` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0952` n `12`; crypto_alt avg `0.133` n `228`; crypto_major avg `-0.0819` n `8`; equity avg `-0.3553` n `86`; fx avg `0.0046` n `6`; index avg `-0.0515` n `23`; metal avg `-0.1059` n `20`; unknown avg `-0.0677` n `764`
- 1h: commodity avg `-0.1009` n `12`; crypto_alt avg `-0.7149` n `228`; crypto_major avg `-0.7439` n `8`; equity avg `-1.066` n `86`; fx avg `0.0144` n `6`; index avg `-0.0529` n `23`; metal avg `0.2238` n `20`; unknown avg `0.0321` n `764`
- 4h: commodity avg `-0.4895` n `12`; crypto_alt avg `-1.2688` n `228`; crypto_major avg `-1.3165` n `8`; equity avg `-1.4673` n `86`; fx avg `-0.0599` n `6`; index avg `-0.0555` n `23`; metal avg `-0.7998` n `20`; unknown avg `0.2725` n `764`
- 24h: commodity avg `-0.6206` n `12`; crypto_alt avg `-1.7607` n `228`; crypto_major avg `-1.5383` n `8`; equity avg `1.8543` n `86`; fx avg `-0.0039` n `6`; index avg `-0.0474` n `23`; metal avg `-1.4769` n `20`; unknown avg `-0.4608` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
