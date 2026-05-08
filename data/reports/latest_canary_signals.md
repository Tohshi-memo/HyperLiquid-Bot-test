# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T22:37:19.036780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0426` n `12`; crypto_alt avg `0.1337` n `228`; crypto_major avg `0.0568` n `8`; equity avg `-0.0071` n `65`; fx avg `-0.0287` n `5`; index avg `-0.0219` n `23`; metal avg `-0.0676` n `18`; unknown avg `-0.0406` n `375`
- 1h: commodity avg `-0.2093` n `12`; crypto_alt avg `0.3462` n `228`; crypto_major avg `0.1823` n `8`; equity avg `0.094` n `65`; fx avg `-0.0264` n `5`; index avg `0.0912` n `23`; metal avg `-0.0721` n `18`; unknown avg `-0.0982` n `375`
- 4h: commodity avg `-0.2714` n `12`; crypto_alt avg `0.5134` n `228`; crypto_major avg `0.1555` n `8`; equity avg `0.7824` n `65`; fx avg `-0.0208` n `5`; index avg `0.1191` n `23`; metal avg `-0.2489` n `18`; unknown avg `-0.4752` n `375`
- 24h: commodity avg `-0.8546` n `12`; crypto_alt avg `4.2322` n `228`; crypto_major avg `2.0654` n `8`; equity avg `4.653` n `65`; fx avg `0.1808` n `5`; index avg `1.7221` n `23`; metal avg `1.1124` n `18`; unknown avg `0.9909` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
