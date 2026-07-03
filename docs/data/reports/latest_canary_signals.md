# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T09:07:33.916577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.1209` n `229`; crypto_major avg `0.3303` n `8`; equity avg `0.0003` n `88`; fx avg `0.0011` n `6`; index avg `-0.0428` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0587` n `765`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `0.2081` n `229`; crypto_major avg `0.2001` n `8`; equity avg `-0.0577` n `88`; fx avg `0.0055` n `6`; index avg `-0.0443` n `25`; metal avg `-0.0666` n `20`; unknown avg `0.0694` n `765`
- 4h: commodity avg `-0.0537` n `12`; crypto_alt avg `0.734` n `229`; crypto_major avg `0.7853` n `8`; equity avg `0.1592` n `88`; fx avg `-0.1404` n `6`; index avg `0.0317` n `25`; metal avg `0.0326` n `20`; unknown avg `0.1279` n `743`
- 24h: commodity avg `0.4028` n `12`; crypto_alt avg `2.3545` n `228`; crypto_major avg `3.5929` n `8`; equity avg `0.2042` n `88`; fx avg `-0.1319` n `6`; index avg `0.2026` n `25`; metal avg `1.2017` n `20`; unknown avg `5.5118` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
