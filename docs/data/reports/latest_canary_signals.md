# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T12:07:28.275276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0556` n `12`; crypto_alt avg `-0.0696` n `233`; crypto_major avg `0.0375` n `8`; equity avg `-0.1921` n `134`; fx avg `0.0072` n `6`; index avg `-0.0494` n `26`; metal avg `-0.0866` n `20`; unknown avg `0.1131` n `796`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.651` n `233`; crypto_major avg `0.6078` n `8`; equity avg `-0.0263` n `134`; fx avg `0.0157` n `6`; index avg `-0.0274` n `26`; metal avg `-0.0496` n `20`; unknown avg `0.5046` n `796`
- 4h: commodity avg `0.0569` n `12`; crypto_alt avg `-0.5045` n `233`; crypto_major avg `-0.428` n `8`; equity avg `-0.8386` n `134`; fx avg `0.0187` n `6`; index avg `-0.211` n `26`; metal avg `-0.1468` n `20`; unknown avg `14.089` n `790`
- 24h: commodity avg `-0.1245` n `12`; crypto_alt avg `0.5732` n `232`; crypto_major avg `1.6854` n `8`; equity avg `0.2433` n `134`; fx avg `-0.1091` n `6`; index avg `-0.1713` n `26`; metal avg `-0.0854` n `20`; unknown avg `1.3165` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
