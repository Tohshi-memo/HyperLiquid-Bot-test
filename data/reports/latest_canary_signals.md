# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T06:52:26.844038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1321` n `13`; crypto_alt avg `0.011` n `236`; crypto_major avg `0.0658` n `8`; equity avg `-0.012` n `151`; fx avg `0.0004` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.0642` n `1191`
- 1h: commodity avg `-0.1934` n `13`; crypto_alt avg `0.0297` n `236`; crypto_major avg `0.1126` n `8`; equity avg `0.0521` n `151`; fx avg `-0.0005` n `6`; index avg `-0.0056` n `26`; metal avg `0.0159` n `20`; unknown avg `0.3976` n `1173`
- 4h: commodity avg `-0.1986` n `13`; crypto_alt avg `0.2271` n `236`; crypto_major avg `0.2913` n `8`; equity avg `0.1395` n `151`; fx avg `-0.0041` n `6`; index avg `0.0294` n `26`; metal avg `0.0133` n `20`; unknown avg `0.6381` n `1167`
- 24h: commodity avg `0.2898` n `13`; crypto_alt avg `-2.0704` n `236`; crypto_major avg `-1.3638` n `8`; equity avg `-3.7688` n `151`; fx avg `0.0627` n `6`; index avg `-0.5841` n `26`; metal avg `-0.2025` n `20`; unknown avg `40.6168` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1806`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.124`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0749`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
