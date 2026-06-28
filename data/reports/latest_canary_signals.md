# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T08:52:25.862988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `0.2991` n `228`; crypto_major avg `0.3812` n `8`; equity avg `0.0744` n `88`; fx avg `0.0025` n `6`; index avg `0.0176` n `23`; metal avg `0.0141` n `20`; unknown avg `0.095` n `764`
- 1h: commodity avg `-0.0983` n `12`; crypto_alt avg `0.4017` n `228`; crypto_major avg `0.6151` n `8`; equity avg `0.115` n `88`; fx avg `-0.0096` n `6`; index avg `0.0467` n `23`; metal avg `0.0192` n `20`; unknown avg `0.2576` n `764`
- 4h: commodity avg `0.0279` n `12`; crypto_alt avg `0.1919` n `228`; crypto_major avg `0.604` n `8`; equity avg `0.2586` n `88`; fx avg `-0.0002` n `6`; index avg `0.0529` n `23`; metal avg `0.0015` n `20`; unknown avg `0.5214` n `724`
- 24h: commodity avg `0.214` n `12`; crypto_alt avg `0.0924` n `228`; crypto_major avg `-0.5327` n `8`; equity avg `0.1248` n `88`; fx avg `-0.0238` n `6`; index avg `-0.061` n `23`; metal avg `-0.0247` n `20`; unknown avg `16.9753` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
