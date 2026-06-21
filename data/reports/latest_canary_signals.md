# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T11:52:25.666130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.1245` n `228`; crypto_major avg `-0.113` n `8`; equity avg `-0.0182` n `78`; fx avg `-0.0003` n `6`; index avg `-0.0023` n `23`; metal avg `0.0008` n `18`; unknown avg `0.0089` n `702`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.5871` n `228`; crypto_major avg `-0.5882` n `8`; equity avg `-0.0817` n `78`; fx avg `0.0976` n `6`; index avg `-0.0038` n `23`; metal avg `-0.0746` n `18`; unknown avg `-0.0825` n `702`
- 4h: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0886` n `228`; crypto_major avg `-0.4479` n `8`; equity avg `-0.1087` n `78`; fx avg `-0.0025` n `6`; index avg `0.0001` n `23`; metal avg `-0.0471` n `18`; unknown avg `-0.2842` n `702`
- 24h: commodity avg `0.0996` n `12`; crypto_alt avg `1.0259` n `228`; crypto_major avg `-0.5035` n `8`; equity avg `0.322` n `78`; fx avg `0.0315` n `6`; index avg `0.0288` n `23`; metal avg `-0.0714` n `18`; unknown avg `0.3391` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
