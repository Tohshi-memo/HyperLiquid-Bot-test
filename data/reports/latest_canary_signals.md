# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T17:52:27.892284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `-0.0477` n `230`; crypto_major avg `0.0081` n `8`; equity avg `0.1585` n `113`; fx avg `-0.0112` n `6`; index avg `0.0075` n `25`; metal avg `-0.0057` n `20`; unknown avg `1.515` n `786`
- 1h: commodity avg `0.0094` n `12`; crypto_alt avg `0.1972` n `230`; crypto_major avg `0.194` n `8`; equity avg `0.3881` n `113`; fx avg `0.0059` n `6`; index avg `0.023` n `25`; metal avg `0.0281` n `20`; unknown avg `0.5514` n `786`
- 4h: commodity avg `0.0585` n `12`; crypto_alt avg `-0.4229` n `230`; crypto_major avg `-0.0628` n `8`; equity avg `0.7725` n `113`; fx avg `-0.0007` n `6`; index avg `-0.0027` n `25`; metal avg `-0.2323` n `20`; unknown avg `0.2872` n `786`
- 24h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0275` n `230`; crypto_major avg `0.9059` n `8`; equity avg `3.9936` n `113`; fx avg `0.0383` n `6`; index avg `0.4166` n `25`; metal avg `0.1792` n `20`; unknown avg `0.1822` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2266`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
