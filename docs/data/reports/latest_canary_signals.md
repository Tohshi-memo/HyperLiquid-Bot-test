# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T20:07:36.189318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `-0.0225` n `229`; crypto_major avg `-0.1625` n `8`; equity avg `0.2091` n `91`; fx avg `0.0033` n `6`; index avg `0.0504` n `25`; metal avg `0.0479` n `20`; unknown avg `0.0837` n `763`
- 1h: commodity avg `0.0436` n `12`; crypto_alt avg `0.2138` n `229`; crypto_major avg `0.1985` n `8`; equity avg `0.2259` n `91`; fx avg `-0.0069` n `6`; index avg `0.0419` n `25`; metal avg `0.0847` n `20`; unknown avg `0.1016` n `761`
- 4h: commodity avg `0.2902` n `12`; crypto_alt avg `-1.1578` n `229`; crypto_major avg `-0.8146` n `8`; equity avg `-0.1853` n `91`; fx avg `-0.0209` n `6`; index avg `0.0114` n `25`; metal avg `-0.2446` n `20`; unknown avg `0.1069` n `761`
- 24h: commodity avg `0.8287` n `12`; crypto_alt avg `-1.7621` n `229`; crypto_major avg `-0.9429` n `8`; equity avg `-3.2224` n `91`; fx avg `-0.2554` n `6`; index avg `-0.5801` n `25`; metal avg `-0.4699` n `20`; unknown avg `-0.2447` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
