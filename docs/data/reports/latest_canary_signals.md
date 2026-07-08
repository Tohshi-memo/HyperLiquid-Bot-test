# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T18:22:32.081946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `0.0087` n `229`; crypto_major avg `0.0611` n `8`; equity avg `0.0485` n `91`; fx avg `-0.0233` n `6`; index avg `0.0172` n `25`; metal avg `0.0428` n `20`; unknown avg `-0.0228` n `764`
- 1h: commodity avg `-0.1594` n `12`; crypto_alt avg `-0.2143` n `229`; crypto_major avg `-0.153` n `8`; equity avg `0.1509` n `91`; fx avg `-0.0137` n `6`; index avg `0.0202` n `25`; metal avg `0.0556` n `20`; unknown avg `-0.066` n `764`
- 4h: commodity avg `-0.4096` n `12`; crypto_alt avg `0.016` n `229`; crypto_major avg `0.0603` n `8`; equity avg `0.0102` n `91`; fx avg `0.0171` n `6`; index avg `0.1017` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.1432` n `764`
- 24h: commodity avg `0.6443` n `12`; crypto_alt avg `-3.1204` n `229`; crypto_major avg `-3.5765` n `8`; equity avg `-0.0847` n `91`; fx avg `0.0164` n `6`; index avg `-0.174` n `25`; metal avg `-1.1916` n `20`; unknown avg `-0.5724` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
