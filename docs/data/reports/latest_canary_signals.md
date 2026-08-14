# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T09:52:28.009587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0916` n `230`; crypto_major avg `0.0036` n `8`; equity avg `0.0576` n `113`; fx avg `-0.0118` n `6`; index avg `0.0099` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0057` n `787`
- 1h: commodity avg `-0.0597` n `12`; crypto_alt avg `-0.2847` n `230`; crypto_major avg `-0.1934` n `8`; equity avg `0.0274` n `113`; fx avg `-0.0195` n `6`; index avg `0.0102` n `25`; metal avg `0.0563` n `20`; unknown avg `-0.1187` n `787`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `-0.5498` n `230`; crypto_major avg `-0.4945` n `8`; equity avg `0.3296` n `113`; fx avg `-0.0056` n `6`; index avg `0.0478` n `25`; metal avg `0.1779` n `20`; unknown avg `-0.1045` n `755`
- 24h: commodity avg `0.0054` n `12`; crypto_alt avg `-1.0487` n `230`; crypto_major avg `-0.9762` n `8`; equity avg `1.7346` n `113`; fx avg `-0.0897` n `6`; index avg `0.3378` n `25`; metal avg `-0.0906` n `20`; unknown avg `0.9184` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
