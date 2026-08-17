# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T21:45:33.059780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `0.0027` n `230`; crypto_major avg `0.0209` n `8`; equity avg `0.007` n `114`; fx avg `0.0013` n `6`; index avg `0.0139` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0574` n `792`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0911` n `230`; crypto_major avg `0.0621` n `8`; equity avg `0.0941` n `114`; fx avg `-0.0144` n `6`; index avg `0.0368` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0739` n `792`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `0.039` n `230`; crypto_major avg `-0.0219` n `8`; equity avg `-0.2291` n `114`; fx avg `-0.0153` n `6`; index avg `-0.0388` n `25`; metal avg `-0.0394` n `20`; unknown avg `-0.1368` n `792`
- 24h: commodity avg `0.4015` n `12`; crypto_alt avg `0.8078` n `230`; crypto_major avg `1.349` n `8`; equity avg `1.1082` n `114`; fx avg `0.0082` n `6`; index avg `0.0643` n `25`; metal avg `0.2286` n `20`; unknown avg `0.276` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
