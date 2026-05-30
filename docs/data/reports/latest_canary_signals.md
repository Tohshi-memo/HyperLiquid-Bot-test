# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T02:07:22.122156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `0.2871` n `228`; crypto_major avg `0.2467` n `8`; equity avg `0.0179` n `69`; fx avg `-0.0063` n `6`; index avg `-0.0027` n `23`; metal avg `0.019` n `18`; unknown avg `0.07` n `419`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.774` n `228`; crypto_major avg `0.7007` n `8`; equity avg `0.1186` n `69`; fx avg `0.0007` n `6`; index avg `-0.0087` n `23`; metal avg `0.0301` n `18`; unknown avg `0.177` n `419`
- 4h: commodity avg `0.3002` n `12`; crypto_alt avg `1.992` n `228`; crypto_major avg `1.4326` n `8`; equity avg `0.3287` n `69`; fx avg `-0.0094` n `6`; index avg `-0.0385` n `23`; metal avg `0.0943` n `18`; unknown avg `-0.3335` n `419`
- 24h: commodity avg `0.0164` n `12`; crypto_alt avg `1.7311` n `228`; crypto_major avg `2.0234` n `8`; equity avg `1.2318` n `69`; fx avg `0.1035` n `6`; index avg `0.1864` n `23`; metal avg `-0.0564` n `18`; unknown avg `0.4888` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
