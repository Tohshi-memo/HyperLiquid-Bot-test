# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T11:52:23.116055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0828` n `12`; crypto_alt avg `0.0537` n `228`; crypto_major avg `0.0828` n `8`; equity avg `0.0614` n `67`; fx avg `0.0064` n `6`; index avg `0.013` n `23`; metal avg `-0.2411` n `18`; unknown avg `0.1051` n `419`
- 1h: commodity avg `0.3686` n `12`; crypto_alt avg `-0.0769` n `228`; crypto_major avg `0.0436` n `8`; equity avg `0.0938` n `67`; fx avg `0.033` n `6`; index avg `0.0565` n `23`; metal avg `-0.2453` n `18`; unknown avg `-0.2962` n `419`
- 4h: commodity avg `0.2678` n `12`; crypto_alt avg `-0.706` n `228`; crypto_major avg `-0.3446` n `8`; equity avg `-0.0804` n `67`; fx avg `-0.0059` n `6`; index avg `-0.0882` n `23`; metal avg `-0.5685` n `18`; unknown avg `-0.3551` n `419`
- 24h: commodity avg `0.7943` n `12`; crypto_alt avg `-5.4428` n `228`; crypto_major avg `-3.9427` n `8`; equity avg `-1.8609` n `67`; fx avg `-0.0772` n `6`; index avg `-1.2415` n `23`; metal avg `-1.4901` n `18`; unknown avg `-1.7388` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
