# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T23:52:34.474475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.2046` n `228`; crypto_major avg `0.2402` n `8`; equity avg `0.1907` n `86`; fx avg `0.0283` n `6`; index avg `0.0504` n `23`; metal avg `0.2045` n `20`; unknown avg `0.1108` n `764`
- 1h: commodity avg `-0.0557` n `12`; crypto_alt avg `-0.0897` n `228`; crypto_major avg `0.1462` n `8`; equity avg `0.0839` n `86`; fx avg `0.0295` n `6`; index avg `0.053` n `23`; metal avg `-0.0518` n `20`; unknown avg `0.5079` n `756`
- 4h: commodity avg `-0.138` n `12`; crypto_alt avg `0.2892` n `228`; crypto_major avg `0.5036` n `8`; equity avg `0.1106` n `86`; fx avg `0.0105` n `6`; index avg `0.0985` n `23`; metal avg `-0.117` n `20`; unknown avg `0.2863` n `756`
- 24h: commodity avg `-0.5021` n `12`; crypto_alt avg `-1.8592` n `228`; crypto_major avg `-2.8255` n `8`; equity avg `-3.0601` n `86`; fx avg `-0.1932` n `6`; index avg `-0.7865` n `23`; metal avg `-1.2468` n `20`; unknown avg `0.832` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
