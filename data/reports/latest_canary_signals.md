# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T21:07:19.900553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0894` n `12`; crypto_alt avg `0.0` n `228`; crypto_major avg `0.0671` n `8`; equity avg `0.0295` n `69`; fx avg `-0.0017` n `6`; index avg `-0.0065` n `23`; metal avg `0.0085` n `18`; unknown avg `0.1445` n `421`
- 1h: commodity avg `0.0961` n `12`; crypto_alt avg `-0.0151` n `228`; crypto_major avg `-0.1756` n `8`; equity avg `0.1146` n `69`; fx avg `-0.003` n `6`; index avg `0.1407` n `23`; metal avg `0.0133` n `18`; unknown avg `0.0696` n `421`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `0.3768` n `228`; crypto_major avg `0.3584` n `8`; equity avg `0.2926` n `69`; fx avg `0.0309` n `6`; index avg `-0.0089` n `23`; metal avg `-0.0014` n `18`; unknown avg `-0.1421` n `421`
- 24h: commodity avg `-0.2113` n `12`; crypto_alt avg `1.4976` n `228`; crypto_major avg `2.4796` n `8`; equity avg `0.9744` n `69`; fx avg `0.0161` n `6`; index avg `0.0609` n `23`; metal avg `0.1505` n `18`; unknown avg `0.3059` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
