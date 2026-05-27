# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T17:52:27.829120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `0.0133` n `8`; equity avg `-0.0105` n `67`; fx avg `0.0011` n `6`; index avg `0.0033` n `23`; metal avg `-0.0228` n `18`; unknown avg `-0.0575` n `418`
- 1h: commodity avg `-0.133` n `12`; crypto_alt avg `-0.7243` n `228`; crypto_major avg `-0.6647` n `8`; equity avg `-0.1281` n `67`; fx avg `0.0125` n `6`; index avg `-0.0717` n `23`; metal avg `-0.1312` n `18`; unknown avg `-0.0845` n `418`
- 4h: commodity avg `0.1175` n `12`; crypto_alt avg `-0.0964` n `228`; crypto_major avg `-0.337` n `8`; equity avg `-0.1464` n `67`; fx avg `-0.003` n `6`; index avg `-0.1567` n `23`; metal avg `0.0335` n `18`; unknown avg `-0.5708` n `418`
- 24h: commodity avg `-1.225` n `12`; crypto_alt avg `-0.8397` n `228`; crypto_major avg `-0.8778` n `8`; equity avg `-0.4697` n `67`; fx avg `-0.0676` n `6`; index avg `-0.5207` n `23`; metal avg `-0.8661` n `18`; unknown avg `-0.81` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
