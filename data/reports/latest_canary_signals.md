# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T12:52:25.347744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `-0.0574` n `230`; crypto_major avg `-0.0167` n `8`; equity avg `-0.0588` n `98`; fx avg `0.003` n `6`; index avg `-0.0288` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0454` n `770`
- 1h: commodity avg `0.3948` n `12`; crypto_alt avg `-0.075` n `230`; crypto_major avg `-0.3288` n `8`; equity avg `-0.2579` n `98`; fx avg `0.0016` n `6`; index avg `-0.0591` n `25`; metal avg `-0.1676` n `20`; unknown avg `0.0183` n `770`
- 4h: commodity avg `0.185` n `12`; crypto_alt avg `0.8394` n `230`; crypto_major avg `0.8572` n `8`; equity avg `0.709` n `98`; fx avg `-0.028` n `6`; index avg `0.1468` n `25`; metal avg `-0.0438` n `20`; unknown avg `0.1822` n `770`
- 24h: commodity avg `-0.4318` n `12`; crypto_alt avg `0.8667` n `230`; crypto_major avg `0.4032` n `8`; equity avg `0.8489` n `97`; fx avg `-0.0435` n `6`; index avg `0.1799` n `25`; metal avg `0.1681` n `20`; unknown avg `0.067` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1006`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
