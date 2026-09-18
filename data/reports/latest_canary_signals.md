# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T07:22:36.778994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1018` n `12`; crypto_alt avg `0.098` n `234`; crypto_major avg `0.0788` n `8`; equity avg `0.0118` n `140`; fx avg `0.0177` n `6`; index avg `0.0199` n `26`; metal avg `0.0334` n `20`; unknown avg `0.1843` n `927`
- 1h: commodity avg `-0.152` n `12`; crypto_alt avg `0.3619` n `234`; crypto_major avg `0.2486` n `8`; equity avg `0.1762` n `140`; fx avg `0.0122` n `6`; index avg `0.0531` n `26`; metal avg `0.0858` n `20`; unknown avg `0.0092` n `907`
- 4h: commodity avg `-0.2561` n `12`; crypto_alt avg `0.5922` n `234`; crypto_major avg `0.823` n `8`; equity avg `0.7177` n `140`; fx avg `-0.0183` n `6`; index avg `0.1096` n `26`; metal avg `0.4328` n `20`; unknown avg `0.1133` n `863`
- 24h: commodity avg `-0.3175` n `12`; crypto_alt avg `4.9883` n `234`; crypto_major avg `3.7768` n `8`; equity avg `2.1838` n `140`; fx avg `0.1374` n `6`; index avg `0.3225` n `26`; metal avg `0.6371` n `20`; unknown avg `2.7195` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
