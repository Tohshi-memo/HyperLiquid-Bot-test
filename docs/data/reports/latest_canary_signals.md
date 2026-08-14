# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T07:22:32.360516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.0289` n `230`; crypto_major avg `0.0902` n `8`; equity avg `-0.026` n `113`; fx avg `0.0098` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0175` n `20`; unknown avg `-0.0135` n `787`
- 1h: commodity avg `0.0824` n `12`; crypto_alt avg `-0.1326` n `230`; crypto_major avg `-0.1157` n `8`; equity avg `0.0773` n `113`; fx avg `0.0428` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0301` n `20`; unknown avg `0.0734` n `787`
- 4h: commodity avg `0.2733` n `12`; crypto_alt avg `-0.4456` n `230`; crypto_major avg `-0.5369` n `8`; equity avg `-0.115` n `113`; fx avg `0.0729` n `6`; index avg `0.0043` n `25`; metal avg `0.0416` n `20`; unknown avg `0.0377` n `755`
- 24h: commodity avg `-0.1644` n `12`; crypto_alt avg `-0.7262` n `230`; crypto_major avg `-0.9996` n `8`; equity avg `1.2891` n `113`; fx avg `-0.0154` n `6`; index avg `0.2821` n `25`; metal avg `-0.2323` n `20`; unknown avg `0.9178` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
