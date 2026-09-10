# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T00:52:31.807631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.2045` n `233`; crypto_major avg `-0.1044` n `8`; equity avg `-0.1234` n `134`; fx avg `-0.0024` n `6`; index avg `-0.0133` n `26`; metal avg `0.0106` n `20`; unknown avg `0.1393` n `797`
- 1h: commodity avg `-0.1262` n `12`; crypto_alt avg `-0.6766` n `233`; crypto_major avg `-0.2665` n `8`; equity avg `-0.2002` n `134`; fx avg `-0.0173` n `6`; index avg `-0.0083` n `26`; metal avg `0.0144` n `20`; unknown avg `-0.3066` n `789`
- 4h: commodity avg `-0.0531` n `12`; crypto_alt avg `-1.9274` n `233`; crypto_major avg `-0.8591` n `8`; equity avg `-0.4271` n `134`; fx avg `-0.0167` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0065` n `20`; unknown avg `132.5841` n `715`
- 24h: commodity avg `0.0117` n `12`; crypto_alt avg `-3.4105` n `233`; crypto_major avg `-2.4048` n `8`; equity avg `-1.0314` n `134`; fx avg `-0.0206` n `6`; index avg `-0.2092` n `26`; metal avg `0.4301` n `20`; unknown avg `0.947` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
