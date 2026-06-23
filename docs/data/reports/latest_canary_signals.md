# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T22:22:34.272393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.0394` n `228`; crypto_major avg `-0.1255` n `8`; equity avg `-0.0125` n `86`; fx avg `-0.0024` n `6`; index avg `-0.0076` n `23`; metal avg `-0.0747` n `20`; unknown avg `0.4053` n `764`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `0.1847` n `228`; crypto_major avg `0.2308` n `8`; equity avg `0.0632` n `86`; fx avg `-0.0169` n `6`; index avg `0.0649` n `23`; metal avg `-0.0883` n `20`; unknown avg `-0.0334` n `764`
- 4h: commodity avg `0.0195` n `12`; crypto_alt avg `0.8081` n `228`; crypto_major avg `0.3805` n `8`; equity avg `-0.0859` n `86`; fx avg `-0.0077` n `6`; index avg `0.0775` n `23`; metal avg `-0.1291` n `20`; unknown avg `1.2508` n `756`
- 24h: commodity avg `-0.4345` n `12`; crypto_alt avg `-2.1459` n `228`; crypto_major avg `-3.2258` n `8`; equity avg `-3.2085` n `86`; fx avg `-0.1682` n `6`; index avg `-0.8686` n `23`; metal avg `-1.2881` n `20`; unknown avg `1.8123` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
