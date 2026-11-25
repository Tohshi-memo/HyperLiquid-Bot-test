# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T23:37:24.509532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `13`; crypto_alt avg `0.0935` n `239`; crypto_major avg `0.0892` n `8`; equity avg `0.1821` n `168`; fx avg `0.0019` n `6`; index avg `0.013` n `27`; metal avg `0.0217` n `20`; unknown avg `0.0259` n `1265`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.1169` n `239`; crypto_major avg `-0.0189` n `8`; equity avg `0.2053` n `168`; fx avg `0.0057` n `6`; index avg `0.017` n `27`; metal avg `-0.0079` n `20`; unknown avg `165.2553` n `1209`
- 4h: commodity avg `0.0786` n `13`; crypto_alt avg `-0.0955` n `239`; crypto_major avg `-0.246` n `8`; equity avg `0.2292` n `168`; fx avg `-0.0208` n `6`; index avg `-0.0005` n `27`; metal avg `0.2642` n `20`; unknown avg `530.2508` n `1143`
- 24h: commodity avg `0.3799` n `13`; crypto_alt avg `2.3629` n `239`; crypto_major avg `1.028` n `8`; equity avg `-0.0885` n `168`; fx avg `0.0417` n `6`; index avg `-0.0503` n `27`; metal avg `0.2311` n `20`; unknown avg `770.3573` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
