# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T03:37:12.596413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.1047` n `228`; crypto_major avg `0.076` n `8`; equity avg `0.0524` n `65`; fx avg `0.0013` n `5`; index avg `-0.0121` n `23`; metal avg `0.0362` n `18`; unknown avg `-0.1834` n `376`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.0228` n `228`; crypto_major avg `-0.0202` n `8`; equity avg `0.1737` n `65`; fx avg `0.0026` n `5`; index avg `-0.0168` n `23`; metal avg `0.081` n `18`; unknown avg `0.0089` n `376`
- 4h: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.2607` n `228`; crypto_major avg `-0.1219` n `8`; equity avg `0.2143` n `65`; fx avg `0.0036` n `5`; index avg `0.071` n `23`; metal avg `0.1331` n `18`; unknown avg `-0.6385` n `376`
- 24h: commodity avg `0.3844` n `12`; crypto_alt avg `-1.462` n `228`; crypto_major avg `-0.7355` n `8`; equity avg `0.8874` n `65`; fx avg `-0.0074` n `5`; index avg `0.3313` n `23`; metal avg `0.2276` n `18`; unknown avg `-0.1673` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
