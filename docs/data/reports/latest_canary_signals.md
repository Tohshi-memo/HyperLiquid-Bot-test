# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T10:07:25.579425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.015` n `13`; crypto_alt avg `-0.0685` n `239`; crypto_major avg `-0.0365` n `8`; equity avg `0.0025` n `168`; fx avg `-0.0001` n `6`; index avg `0.0048` n `27`; metal avg `0.0035` n `20`; unknown avg `22.1855` n `1255`
- 1h: commodity avg `0.0029` n `13`; crypto_alt avg `-0.3807` n `239`; crypto_major avg `-0.0682` n `8`; equity avg `0.0693` n `168`; fx avg `-0.0116` n `6`; index avg `0.0097` n `27`; metal avg `0.0217` n `20`; unknown avg `19.5908` n `1257`
- 4h: commodity avg `-0.0285` n `13`; crypto_alt avg `0.0493` n `239`; crypto_major avg `-0.211` n `8`; equity avg `0.1659` n `168`; fx avg `-0.014` n `6`; index avg `-0.0019` n `27`; metal avg `0.0525` n `20`; unknown avg `228.2778` n `1205`
- 24h: commodity avg `-0.6059` n `13`; crypto_alt avg `-3.3785` n `239`; crypto_major avg `-3.056` n `8`; equity avg `-0.094` n `168`; fx avg `-0.0851` n `6`; index avg `0.0556` n `27`; metal avg `-0.2134` n `20`; unknown avg `375.4771` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
