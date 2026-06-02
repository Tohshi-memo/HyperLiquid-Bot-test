# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T00:07:23.513893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.86` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0425` n `12`; crypto_alt avg `0.0064` n `228`; crypto_major avg `-0.1128` n `8`; equity avg `-0.2516` n `69`; fx avg `0.044` n `6`; index avg `-0.0378` n `23`; metal avg `-0.1043` n `18`; unknown avg `0.6828` n `422`
- 1h: commodity avg `-0.176` n `12`; crypto_alt avg `-0.0581` n `228`; crypto_major avg `-0.1836` n `8`; equity avg `-0.3493` n `69`; fx avg `0.0365` n `6`; index avg `-0.0996` n `23`; metal avg `-0.0808` n `18`; unknown avg `0.092` n `422`
- 4h: commodity avg `-0.2574` n `12`; crypto_alt avg `-0.2775` n `228`; crypto_major avg `-0.0261` n `8`; equity avg `-0.3864` n `69`; fx avg `0.0219` n `6`; index avg `-0.2688` n `23`; metal avg `-0.0659` n `18`; unknown avg `0.756` n `422`
- 24h: commodity avg `-0.0152` n `12`; crypto_alt avg `-0.1272` n `228`; crypto_major avg `-1.0115` n `8`; equity avg `-0.3896` n `69`; fx avg `0.0811` n `6`; index avg `-0.0399` n `23`; metal avg `-0.478` n `18`; unknown avg `2.3224` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
