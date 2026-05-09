# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T19:22:19.985706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `8.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `-0.0801` n `228`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0203` n `65`; fx avg `0.0` n `5`; index avg `-0.009` n `23`; metal avg `-0.0021` n `18`; unknown avg `0.2876` n `376`
- 1h: commodity avg `0.0228` n `12`; crypto_alt avg `0.0489` n `228`; crypto_major avg `0.0223` n `8`; equity avg `0.0604` n `65`; fx avg `-0.0076` n `5`; index avg `0.0183` n `23`; metal avg `0.0135` n `18`; unknown avg `0.2578` n `376`
- 4h: commodity avg `-0.0374` n `12`; crypto_alt avg `0.7184` n `228`; crypto_major avg `0.513` n `8`; equity avg `0.1597` n `65`; fx avg `-0.0414` n `5`; index avg `0.0578` n `23`; metal avg `0.1038` n `18`; unknown avg `0.4008` n `376`
- 24h: commodity avg `0.153` n `12`; crypto_alt avg `0.4875` n `228`; crypto_major avg `0.2944` n `8`; equity avg `1.1262` n `65`; fx avg `-0.0358` n `5`; index avg `0.3633` n `23`; metal avg `-0.1283` n `18`; unknown avg `0.4936` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
