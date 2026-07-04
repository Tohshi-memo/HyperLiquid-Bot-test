# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T16:07:29.039055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.2197` n `229`; crypto_major avg `-0.0284` n `8`; equity avg `0.0159` n `88`; fx avg `0.0037` n `6`; index avg `0.0016` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0358` n `765`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.6068` n `229`; crypto_major avg `0.2839` n `8`; equity avg `0.0713` n `88`; fx avg `-0.0034` n `6`; index avg `0.0015` n `25`; metal avg `0.0148` n `20`; unknown avg `0.1808` n `765`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.8916` n `229`; crypto_major avg `0.9039` n `8`; equity avg `0.0726` n `88`; fx avg `0.0198` n `6`; index avg `0.0166` n `25`; metal avg `0.031` n `20`; unknown avg `0.0458` n `759`
- 24h: commodity avg `0.0196` n `12`; crypto_alt avg `1.5755` n `229`; crypto_major avg `1.9399` n `8`; equity avg `0.288` n `88`; fx avg `-0.0082` n `6`; index avg `0.0093` n `25`; metal avg `0.1102` n `20`; unknown avg `1.5601` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
