# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T11:22:35.461646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.0944` n `230`; crypto_major avg `0.1837` n `8`; equity avg `-0.0028` n `114`; fx avg `0.002` n `6`; index avg `0.0021` n `25`; metal avg `0.0112` n `20`; unknown avg `0.0941` n `795`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.2317` n `230`; crypto_major avg `0.3587` n `8`; equity avg `0.4446` n `114`; fx avg `0.0042` n `6`; index avg `0.0588` n `25`; metal avg `0.0462` n `20`; unknown avg `0.299` n `795`
- 4h: commodity avg `0.0103` n `12`; crypto_alt avg `0.255` n `230`; crypto_major avg `-0.0069` n `8`; equity avg `-0.732` n `114`; fx avg `-0.0281` n `6`; index avg `-0.0946` n `25`; metal avg `-0.0748` n `20`; unknown avg `0.0267` n `795`
- 24h: commodity avg `0.5076` n `12`; crypto_alt avg `-0.7225` n `230`; crypto_major avg `0.1544` n `8`; equity avg `-2.3911` n `114`; fx avg `-0.0485` n `6`; index avg `-0.4985` n `25`; metal avg `-0.2297` n `20`; unknown avg `-0.0164` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
