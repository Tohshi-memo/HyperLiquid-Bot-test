# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T01:37:28.788398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.1628` n `233`; crypto_major avg `0.1795` n `8`; equity avg `0.1325` n `134`; fx avg `-0.013` n `6`; index avg `0.0139` n `26`; metal avg `0.0454` n `20`; unknown avg `0.3109` n `797`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.1522` n `233`; crypto_major avg `-0.0503` n `8`; equity avg `0.5338` n `134`; fx avg `-0.0105` n `6`; index avg `0.0912` n `26`; metal avg `0.1516` n `20`; unknown avg `0.1439` n `795`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `0.0028` n `233`; crypto_major avg `0.4086` n `8`; equity avg `0.511` n `134`; fx avg `-0.0202` n `6`; index avg `0.1152` n `26`; metal avg `0.0937` n `20`; unknown avg `0.6623` n `757`
- 24h: commodity avg `0.1868` n `12`; crypto_alt avg `-1.2094` n `232`; crypto_major avg `-0.0033` n `8`; equity avg `0.5563` n `134`; fx avg `0.0259` n `6`; index avg `-0.1119` n `26`; metal avg `-0.3824` n `20`; unknown avg `0.2386` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
