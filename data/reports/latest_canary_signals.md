# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:52:28.457440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0263` n `231`; crypto_major avg `0.0305` n `8`; equity avg `0.0082` n `122`; fx avg `0.0211` n `6`; index avg `-0.0005` n `25`; metal avg `0.0474` n `20`; unknown avg `0.0799` n `793`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `0.5669` n `231`; crypto_major avg `0.5985` n `8`; equity avg `0.0528` n `122`; fx avg `-0.0235` n `6`; index avg `0.0031` n `25`; metal avg `0.0288` n `20`; unknown avg `0.2942` n `793`
- 4h: commodity avg `0.08` n `12`; crypto_alt avg `0.0561` n `231`; crypto_major avg `0.1294` n `8`; equity avg `0.1465` n `122`; fx avg `0.0187` n `6`; index avg `0.0204` n `25`; metal avg `0.0082` n `20`; unknown avg `0.4536` n `777`
- 24h: commodity avg `-0.1611` n `12`; crypto_alt avg `2.0604` n `231`; crypto_major avg `0.6722` n `8`; equity avg `-1.1907` n `122`; fx avg `-0.1543` n `6`; index avg `-0.1076` n `25`; metal avg `0.1654` n `20`; unknown avg `5.6954` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
