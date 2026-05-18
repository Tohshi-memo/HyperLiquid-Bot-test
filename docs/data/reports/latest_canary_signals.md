# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T04:22:13.758733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0649` n `12`; crypto_alt avg `0.0022` n `228`; crypto_major avg `-0.0295` n `8`; equity avg `0.0415` n `66`; fx avg `0.0034` n `5`; index avg `0.062` n `23`; metal avg `0.0243` n `18`; unknown avg `0.2386` n `383`
- 1h: commodity avg `0.0862` n `12`; crypto_alt avg `-0.1262` n `228`; crypto_major avg `0.0784` n `8`; equity avg `0.2075` n `66`; fx avg `0.0159` n `5`; index avg `0.1532` n `23`; metal avg `0.4208` n `18`; unknown avg `-0.1706` n `383`
- 4h: commodity avg `0.378` n `12`; crypto_alt avg `0.2263` n `228`; crypto_major avg `-0.5378` n `8`; equity avg `0.6662` n `66`; fx avg `0.088` n `5`; index avg `0.3835` n `23`; metal avg `-0.139` n `18`; unknown avg `-0.6137` n `383`
- 24h: commodity avg `2.7204` n `12`; crypto_alt avg `-10.9383` n `228`; crypto_major avg `-3.4815` n `8`; equity avg `-2.9242` n `65`; fx avg `-0.0607` n `5`; index avg `-1.6706` n `23`; metal avg `-6.0301` n `18`; unknown avg `550.0589` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
