# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T03:07:25.995475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.1407` n `229`; crypto_major avg `0.1524` n `8`; equity avg `0.1134` n `91`; fx avg `-0.0241` n `6`; index avg `0.0409` n `25`; metal avg `0.0493` n `20`; unknown avg `0.9975` n `763`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.4779` n `229`; crypto_major avg `-0.5046` n `8`; equity avg `-0.2414` n `91`; fx avg `-0.0296` n `6`; index avg `-0.045` n `25`; metal avg `-0.0592` n `20`; unknown avg `4.8527` n `763`
- 4h: commodity avg `0.0535` n `12`; crypto_alt avg `-1.1358` n `229`; crypto_major avg `-1.1792` n `8`; equity avg `-1.1354` n `91`; fx avg `-0.0986` n `6`; index avg `-0.3131` n `25`; metal avg `-0.2295` n `20`; unknown avg `1.9988` n `761`
- 24h: commodity avg `0.3221` n `12`; crypto_alt avg `-0.1916` n `229`; crypto_major avg `-0.8564` n `8`; equity avg `-0.7644` n `90`; fx avg `-0.0176` n `6`; index avg `-0.1419` n `25`; metal avg `-0.2041` n `20`; unknown avg `-0.2354` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
