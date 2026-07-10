# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T07:52:33.564830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0077` n `229`; crypto_major avg `-0.0069` n `8`; equity avg `-0.0583` n `91`; fx avg `-0.0021` n `6`; index avg `-0.014` n `25`; metal avg `-0.0542` n `20`; unknown avg `0.0088` n `765`
- 1h: commodity avg `-0.2118` n `12`; crypto_alt avg `0.0551` n `229`; crypto_major avg `-0.0381` n `8`; equity avg `-0.2834` n `91`; fx avg `0.0212` n `6`; index avg `-0.0354` n `25`; metal avg `-0.072` n `20`; unknown avg `0.0115` n `765`
- 4h: commodity avg `-0.2681` n `12`; crypto_alt avg `-0.1794` n `229`; crypto_major avg `-0.1958` n `8`; equity avg `-0.781` n `91`; fx avg `-0.072` n `6`; index avg `-0.153` n `25`; metal avg `-0.1342` n `20`; unknown avg `-0.0044` n `733`
- 24h: commodity avg `-0.9537` n `12`; crypto_alt avg `0.6926` n `229`; crypto_major avg `0.8639` n `8`; equity avg `0.2219` n `91`; fx avg `-0.1182` n `6`; index avg `0.1534` n `25`; metal avg `0.203` n `20`; unknown avg `0.1243` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
