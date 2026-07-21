# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T00:37:24.368978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.1357` n `230`; crypto_major avg `0.1808` n `8`; equity avg `0.2556` n `98`; fx avg `-0.0088` n `6`; index avg `0.0569` n `25`; metal avg `0.0455` n `20`; unknown avg `-0.0728` n `771`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `0.2483` n `230`; crypto_major avg `0.2585` n `8`; equity avg `0.1242` n `98`; fx avg `0.0236` n `6`; index avg `-0.0342` n `25`; metal avg `0.0769` n `20`; unknown avg `-0.0872` n `770`
- 4h: commodity avg `0.0428` n `12`; crypto_alt avg `0.0767` n `230`; crypto_major avg `0.1094` n `8`; equity avg `0.3403` n `98`; fx avg `0.0095` n `6`; index avg `0.0108` n `25`; metal avg `0.0475` n `20`; unknown avg `-0.4904` n `770`
- 24h: commodity avg `-0.2944` n `12`; crypto_alt avg `1.1479` n `230`; crypto_major avg `0.9701` n `8`; equity avg `-0.7604` n `98`; fx avg `-0.1628` n `6`; index avg `-0.1664` n `25`; metal avg `0.146` n `20`; unknown avg `-0.0732` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1101`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.106`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0949`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `666`, weak_sample_signal
