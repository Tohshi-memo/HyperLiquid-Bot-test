# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T14:22:28.539513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.4148` n `231`; crypto_major avg `0.2372` n `8`; equity avg `0.4898` n `127`; fx avg `0.0134` n `6`; index avg `0.0651` n `26`; metal avg `0.0597` n `20`; unknown avg `0.0956` n `793`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.3429` n `231`; crypto_major avg `-0.4238` n `8`; equity avg `-0.1539` n `127`; fx avg `-0.0232` n `6`; index avg `0.0071` n `26`; metal avg `-0.2412` n `20`; unknown avg `-0.1356` n `793`
- 4h: commodity avg `-0.1533` n `12`; crypto_alt avg `-0.2389` n `231`; crypto_major avg `-0.0861` n `8`; equity avg `-0.1746` n `127`; fx avg `0.0037` n `6`; index avg `0.0385` n `26`; metal avg `-0.1421` n `20`; unknown avg `-0.1587` n `792`
- 24h: commodity avg `-0.2975` n `12`; crypto_alt avg `-1.839` n `231`; crypto_major avg `-1.3954` n `8`; equity avg `-0.9942` n `127`; fx avg `-0.1134` n `6`; index avg `0.0502` n `26`; metal avg `0.5551` n `20`; unknown avg `0.1949` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
