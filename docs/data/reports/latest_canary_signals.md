# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T05:07:28.062591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.036` n `230`; crypto_major avg `-0.0106` n `8`; equity avg `-0.0809` n `113`; fx avg `-0.0139` n `6`; index avg `-0.0254` n `25`; metal avg `-0.0442` n `20`; unknown avg `0.3398` n `787`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.0207` n `230`; crypto_major avg `-0.0718` n `8`; equity avg `-0.0623` n `113`; fx avg `0.0115` n `6`; index avg `-0.0202` n `25`; metal avg `-0.0489` n `20`; unknown avg `-0.0861` n `787`
- 4h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.3241` n `230`; crypto_major avg `-0.348` n `8`; equity avg `-0.1914` n `113`; fx avg `-0.0181` n `6`; index avg `-0.0292` n `25`; metal avg `-0.0194` n `20`; unknown avg `-0.2727` n `787`
- 24h: commodity avg `-0.4201` n `12`; crypto_alt avg `-0.36` n `230`; crypto_major avg `-0.4467` n `8`; equity avg `0.5877` n `113`; fx avg `0.0242` n `6`; index avg `0.1679` n `25`; metal avg `-0.5774` n `20`; unknown avg `0.8093` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2433`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
