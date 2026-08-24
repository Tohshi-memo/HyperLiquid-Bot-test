# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T11:07:31.517122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.2041` n `231`; crypto_major avg `-0.0679` n `8`; equity avg `-0.2596` n `122`; fx avg `0.0059` n `6`; index avg `-0.0286` n `25`; metal avg `-0.0185` n `20`; unknown avg `-0.0676` n `793`
- 1h: commodity avg `0.0481` n `12`; crypto_alt avg `-0.4638` n `231`; crypto_major avg `-0.1999` n `8`; equity avg `-0.5091` n `122`; fx avg `0.017` n `6`; index avg `-0.0687` n `25`; metal avg `-0.041` n `20`; unknown avg `-0.0875` n `793`
- 4h: commodity avg `0.1893` n `12`; crypto_alt avg `-0.1237` n `231`; crypto_major avg `-0.4292` n `8`; equity avg `-0.2844` n `122`; fx avg `-0.0046` n `6`; index avg `-0.0234` n `25`; metal avg `-0.0892` n `20`; unknown avg `0.3665` n `793`
- 24h: commodity avg `-0.1481` n `12`; crypto_alt avg `0.9741` n `231`; crypto_major avg `0.2362` n `8`; equity avg `-1.6965` n `122`; fx avg `-0.1118` n `6`; index avg `-0.1814` n `25`; metal avg `0.1219` n `20`; unknown avg `6.1896` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
