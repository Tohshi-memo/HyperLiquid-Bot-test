# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T22:22:25.750960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.2506` n `228`; crypto_major avg `0.2853` n `8`; equity avg `0.0194` n `78`; fx avg `-0.0031` n `6`; index avg `0.0172` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.2262` n `701`
- 1h: commodity avg `-0.0349` n `12`; crypto_alt avg `0.2978` n `228`; crypto_major avg `0.4538` n `8`; equity avg `0.0535` n `78`; fx avg `0.0067` n `6`; index avg `0.0197` n `23`; metal avg `0.0173` n `18`; unknown avg `0.5045` n `701`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `0.3814` n `228`; crypto_major avg `0.7406` n `8`; equity avg `0.2268` n `78`; fx avg `0.0005` n `6`; index avg `0.0223` n `23`; metal avg `0.0302` n `18`; unknown avg `-0.3354` n `701`
- 24h: commodity avg `0.0959` n `12`; crypto_alt avg `1.0623` n `228`; crypto_major avg `1.626` n `8`; equity avg `0.5852` n `78`; fx avg `0.0708` n `6`; index avg `0.0892` n `23`; metal avg `-0.0313` n `18`; unknown avg `-0.4588` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
