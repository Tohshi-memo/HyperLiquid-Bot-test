# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T13:22:26.204613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0406` n `12`; crypto_alt avg `-0.0706` n `230`; crypto_major avg `-0.0719` n `8`; equity avg `0.1699` n `113`; fx avg `0.0027` n `6`; index avg `0.0218` n `25`; metal avg `-0.0341` n `20`; unknown avg `0.0914` n `786`
- 1h: commodity avg `-0.2111` n `12`; crypto_alt avg `-0.0968` n `230`; crypto_major avg `-0.2865` n `8`; equity avg `0.788` n `113`; fx avg `-0.0209` n `6`; index avg `0.1506` n `25`; metal avg `0.054` n `20`; unknown avg `-0.0044` n `786`
- 4h: commodity avg `-0.1058` n `12`; crypto_alt avg `0.3374` n `230`; crypto_major avg `0.37` n `8`; equity avg `1.0842` n `113`; fx avg `-0.0134` n `6`; index avg `0.1689` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0836` n `786`
- 24h: commodity avg `0.2111` n `12`; crypto_alt avg `-0.7146` n `230`; crypto_major avg `0.8008` n `8`; equity avg `3.121` n `113`; fx avg `0.0258` n `6`; index avg `0.3485` n `25`; metal avg `0.2455` n `20`; unknown avg `-0.1421` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.211`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
