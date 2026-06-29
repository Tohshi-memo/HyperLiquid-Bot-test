# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T23:22:29.752061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.09` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `-0.1231` n `228`; crypto_major avg `-0.1417` n `8`; equity avg `-0.0045` n `88`; fx avg `-0.001` n `6`; index avg `0.0077` n `23`; metal avg `0.0201` n `20`; unknown avg `0.026` n `765`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.3576` n `228`; crypto_major avg `-0.3536` n `8`; equity avg `-0.0002` n `88`; fx avg `0.0116` n `6`; index avg `0.0113` n `23`; metal avg `0.0749` n `20`; unknown avg `0.1443` n `765`
- 4h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.7399` n `228`; crypto_major avg `-0.4044` n `8`; equity avg `0.2283` n `88`; fx avg `0.0325` n `6`; index avg `0.0211` n `23`; metal avg `0.1443` n `20`; unknown avg `0.5682` n `763`
- 24h: commodity avg `-0.2165` n `12`; crypto_alt avg `1.7213` n `228`; crypto_major avg `3.0537` n `8`; equity avg `1.7512` n `88`; fx avg `0.216` n `6`; index avg `0.1061` n `23`; metal avg `-0.177` n `20`; unknown avg `1.905` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
