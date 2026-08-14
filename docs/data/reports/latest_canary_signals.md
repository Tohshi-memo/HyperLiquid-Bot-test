# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T06:07:30.994354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0799` n `12`; crypto_alt avg `-0.0228` n `230`; crypto_major avg `-0.0597` n `8`; equity avg `-0.0957` n `113`; fx avg `-0.0063` n `6`; index avg `-0.0008` n `25`; metal avg `0.0372` n `20`; unknown avg `-0.0344` n `755`
- 1h: commodity avg `0.1711` n `12`; crypto_alt avg `-0.0348` n `230`; crypto_major avg `-0.064` n `8`; equity avg `-0.0111` n `113`; fx avg `-0.0263` n `6`; index avg `0.0516` n `25`; metal avg `0.1441` n `20`; unknown avg `0.0615` n `755`
- 4h: commodity avg `0.2402` n `12`; crypto_alt avg `-0.5064` n `230`; crypto_major avg `-0.4558` n `8`; equity avg `-0.114` n `113`; fx avg `-0.0168` n `6`; index avg `0.0096` n `25`; metal avg `0.1555` n `20`; unknown avg `-0.1166` n `755`
- 24h: commodity avg `-0.2617` n `12`; crypto_alt avg `-0.4298` n `230`; crypto_major avg `-0.6434` n `8`; equity avg `0.7909` n `113`; fx avg `-0.0151` n `6`; index avg `0.2692` n `25`; metal avg `-0.3168` n `20`; unknown avg `0.8768` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2387`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
