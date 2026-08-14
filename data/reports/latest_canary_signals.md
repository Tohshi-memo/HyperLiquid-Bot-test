# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T13:07:25.697850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.1035` n `230`; crypto_major avg `-0.0393` n `8`; equity avg `0.0233` n `114`; fx avg `0.008` n `6`; index avg `0.0042` n `25`; metal avg `0.0519` n `20`; unknown avg `-0.0135` n `786`
- 1h: commodity avg `-0.0894` n `12`; crypto_alt avg `0.0305` n `230`; crypto_major avg `-0.1917` n `8`; equity avg `0.0725` n `114`; fx avg `-0.0132` n `6`; index avg `0.0034` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.0571` n `786`
- 4h: commodity avg `-0.1618` n `12`; crypto_alt avg `-0.1485` n `230`; crypto_major avg `-0.5076` n `8`; equity avg `0.3625` n `114`; fx avg `0.0134` n `6`; index avg `0.051` n `25`; metal avg `0.1579` n `20`; unknown avg `3.7773` n `786`
- 24h: commodity avg `0.0502` n `12`; crypto_alt avg `-0.784` n `230`; crypto_major avg `-1.2241` n `8`; equity avg `1.7268` n `114`; fx avg `-0.033` n `6`; index avg `0.3082` n `25`; metal avg `-0.0879` n `20`; unknown avg `0.8677` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
