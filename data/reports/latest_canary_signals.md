# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T10:22:20.556509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1671` n `12`; crypto_alt avg `0.435` n `228`; crypto_major avg `0.2033` n `8`; equity avg `0.0207` n `69`; fx avg `-0.0101` n `6`; index avg `0.0561` n `23`; metal avg `-0.1323` n `18`; unknown avg `0.044` n `422`
- 1h: commodity avg `0.3404` n `12`; crypto_alt avg `0.4597` n `228`; crypto_major avg `0.1764` n `8`; equity avg `0.1193` n `69`; fx avg `0.0022` n `6`; index avg `0.0815` n `23`; metal avg `-0.1884` n `18`; unknown avg `-0.1525` n `422`
- 4h: commodity avg `0.1799` n `12`; crypto_alt avg `0.045` n `228`; crypto_major avg `-0.4874` n `8`; equity avg `0.211` n `69`; fx avg `0.0021` n `6`; index avg `0.2918` n `23`; metal avg `-0.3072` n `18`; unknown avg `-0.4994` n `422`
- 24h: commodity avg `-0.9082` n `12`; crypto_alt avg `-0.1276` n `228`; crypto_major avg `-1.9411` n `8`; equity avg `0.6171` n `69`; fx avg `0.1075` n `6`; index avg `0.0785` n `23`; metal avg `0.6684` n `18`; unknown avg `0.2032` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
