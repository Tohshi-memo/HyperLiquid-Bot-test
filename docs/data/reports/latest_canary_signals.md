# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T05:52:25.551888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.0109` n `230`; crypto_major avg `0.0794` n `8`; equity avg `-0.0646` n `113`; fx avg `-0.0037` n `6`; index avg `0.0029` n `25`; metal avg `-0.0798` n `20`; unknown avg `-0.232` n `787`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `0.2072` n `230`; crypto_major avg `0.3653` n `8`; equity avg `0.0086` n `113`; fx avg `0.0` n `6`; index avg `-0.0194` n `25`; metal avg `-0.0533` n `20`; unknown avg `2.4527` n `787`
- 4h: commodity avg `0.1491` n `12`; crypto_alt avg `0.4966` n `230`; crypto_major avg `0.8418` n `8`; equity avg `0.1546` n `113`; fx avg `0.0093` n `6`; index avg `0.0155` n `25`; metal avg `-0.1137` n `20`; unknown avg `3.2929` n `786`
- 24h: commodity avg `-0.1359` n `12`; crypto_alt avg `-0.8132` n `230`; crypto_major avg `0.3289` n `8`; equity avg `2.5777` n `113`; fx avg `-0.0541` n `6`; index avg `0.2912` n `25`; metal avg `-0.1136` n `20`; unknown avg `0.1726` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.245`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
