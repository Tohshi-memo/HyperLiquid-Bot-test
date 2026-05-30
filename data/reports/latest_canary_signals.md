# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T20:40:58.753693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `-0.0303` n `228`; crypto_major avg `-0.0641` n `8`; equity avg `0.0298` n `69`; fx avg `-0.0008` n `6`; index avg `0.0024` n `23`; metal avg `0.0085` n `18`; unknown avg `0.0047` n `421`
- 1h: commodity avg `0.0027` n `12`; crypto_alt avg `0.2006` n `228`; crypto_major avg `-0.0752` n `8`; equity avg `0.0843` n `69`; fx avg `0.001` n `6`; index avg `-0.0441` n `23`; metal avg `0.0135` n `18`; unknown avg `-0.2951` n `421`
- 4h: commodity avg `0.008` n `12`; crypto_alt avg `0.276` n `228`; crypto_major avg `0.2374` n `8`; equity avg `0.2407` n `69`; fx avg `0.0014` n `6`; index avg `-0.0262` n `23`; metal avg `-0.0001` n `18`; unknown avg `-0.4069` n `421`
- 24h: commodity avg `-0.0787` n `12`; crypto_alt avg `1.3882` n `228`; crypto_major avg `2.3485` n `8`; equity avg `0.9232` n `69`; fx avg `0.0049` n `6`; index avg `0.0159` n `23`; metal avg `-0.0008` n `18`; unknown avg `0.1879` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
