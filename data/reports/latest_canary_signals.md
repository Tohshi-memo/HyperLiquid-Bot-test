# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T09:22:26.321590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `-0.1307` n `228`; crypto_major avg `-0.1245` n `8`; equity avg `0.0261` n `86`; fx avg `0.0109` n `6`; index avg `-0.0109` n `23`; metal avg `0.0457` n `20`; unknown avg `-0.0954` n `764`
- 1h: commodity avg `-0.012` n `12`; crypto_alt avg `-0.0053` n `228`; crypto_major avg `-0.0017` n `8`; equity avg `-0.064` n `86`; fx avg `0.0279` n `6`; index avg `-0.0139` n `23`; metal avg `-0.0339` n `20`; unknown avg `-0.136` n `764`
- 4h: commodity avg `-0.1464` n `12`; crypto_alt avg `-0.093` n `228`; crypto_major avg `-0.1934` n `8`; equity avg `-0.0202` n `86`; fx avg `0.0456` n `6`; index avg `-0.0038` n `23`; metal avg `-0.0354` n `20`; unknown avg `-0.0889` n `740`
- 24h: commodity avg `-0.5517` n `12`; crypto_alt avg `0.1378` n `228`; crypto_major avg `0.0319` n `8`; equity avg `4.7521` n `86`; fx avg `-0.0002` n `6`; index avg `0.0485` n `23`; metal avg `-0.4071` n `20`; unknown avg `0.0027` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
