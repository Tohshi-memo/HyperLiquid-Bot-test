# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T11:07:31.052184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.1383` n `228`; crypto_major avg `0.1446` n `8`; equity avg `0.0291` n `88`; fx avg `0.0057` n `6`; index avg `0.0008` n `23`; metal avg `0.0074` n `20`; unknown avg `-0.2521` n `764`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `0.0853` n `228`; crypto_major avg `0.0541` n `8`; equity avg `0.0334` n `88`; fx avg `0.002` n `6`; index avg `-0.0003` n `23`; metal avg `0.0016` n `20`; unknown avg `-0.5125` n `764`
- 4h: commodity avg `-0.1155` n `12`; crypto_alt avg `0.1892` n `228`; crypto_major avg `0.3448` n `8`; equity avg `0.2258` n `88`; fx avg `0.0249` n `6`; index avg `0.0587` n `23`; metal avg `0.0132` n `20`; unknown avg `-0.8611` n `742`
- 24h: commodity avg `0.1613` n `12`; crypto_alt avg `-0.027` n `228`; crypto_major avg `-0.6996` n `8`; equity avg `0.0457` n `88`; fx avg `0.0005` n `6`; index avg `-0.0647` n `23`; metal avg `-0.0221` n `20`; unknown avg `15.7973` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
