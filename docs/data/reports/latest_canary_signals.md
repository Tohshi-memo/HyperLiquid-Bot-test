# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T19:37:18.935733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1074` n `12`; crypto_alt avg `-0.2044` n `228`; crypto_major avg `-0.1629` n `8`; equity avg `-0.0024` n `69`; fx avg `0.0046` n `6`; index avg `-0.0029` n `23`; metal avg `-0.0074` n `18`; unknown avg `-0.6377` n `421`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.1103` n `228`; crypto_major avg `-0.0482` n `8`; equity avg `0.0966` n `69`; fx avg `0.0098` n `6`; index avg `0.0253` n `23`; metal avg `-0.0185` n `18`; unknown avg `0.3063` n `421`
- 4h: commodity avg `-0.4796` n `12`; crypto_alt avg `0.4539` n `228`; crypto_major avg `0.7682` n `8`; equity avg `0.0254` n `69`; fx avg `-0.0118` n `6`; index avg `-0.0094` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.0539` n `421`
- 24h: commodity avg `-0.0641` n `12`; crypto_alt avg `1.4848` n `228`; crypto_major avg `2.383` n `8`; equity avg `1.1144` n `69`; fx avg `-0.0067` n `6`; index avg `0.078` n `23`; metal avg `-0.1572` n `18`; unknown avg `0.0457` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
