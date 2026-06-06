# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T12:22:21.174748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1951` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.2759` n `228`; crypto_major avg `-0.2487` n `8`; equity avg `0.1409` n `74`; fx avg `-0.0005` n `6`; index avg `0.0238` n `23`; metal avg `-0.0314` n `18`; unknown avg `-0.0565` n `425`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.2766` n `228`; crypto_major avg `0.3084` n `8`; equity avg `0.3866` n `74`; fx avg `0.0064` n `6`; index avg `0.236` n `23`; metal avg `0.0573` n `18`; unknown avg `0.0444` n `421`
- 4h: commodity avg `0.1404` n `12`; crypto_alt avg `-0.6402` n `228`; crypto_major avg `-0.8242` n `8`; equity avg `0.6499` n `74`; fx avg `0.0086` n `6`; index avg `0.3709` n `23`; metal avg `0.0217` n `18`; unknown avg `-0.1972` n `421`
- 24h: commodity avg `-1.0639` n `12`; crypto_alt avg `-3.4832` n `228`; crypto_major avg `-3.4206` n `8`; equity avg `-6.2384` n `74`; fx avg `-0.2893` n `6`; index avg `-3.8436` n `23`; metal avg `-4.8139` n `18`; unknown avg `0.0978` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
