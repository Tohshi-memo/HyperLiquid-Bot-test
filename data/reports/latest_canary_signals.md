# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T23:52:25.959606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `-0.0846` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `-0.1057` n `98`; fx avg `0.0112` n `6`; index avg `-0.1109` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0393` n `770`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `0.2377` n `8`; equity avg `0.0338` n `98`; fx avg `0.0201` n `6`; index avg `-0.0278` n `25`; metal avg `0.0436` n `20`; unknown avg `0.1481` n `770`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `0.001` n `230`; crypto_major avg `0.043` n `8`; equity avg `-0.0895` n `98`; fx avg `-0.0187` n `6`; index avg `-0.1066` n `25`; metal avg `-0.0279` n `20`; unknown avg `-0.275` n `770`
- 24h: commodity avg `-0.3261` n `12`; crypto_alt avg `1.389` n `230`; crypto_major avg `0.9657` n `8`; equity avg `-0.3303` n `98`; fx avg `-0.1818` n `6`; index avg `-0.0532` n `25`; metal avg `0.1958` n `20`; unknown avg `-0.0781` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
