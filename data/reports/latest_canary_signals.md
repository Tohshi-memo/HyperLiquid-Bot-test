# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T13:52:26.768226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.145` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.186` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1054` n `12`; crypto_alt avg `-0.6754` n `231`; crypto_major avg `-0.7444` n `8`; equity avg `-0.7208` n `122`; fx avg `-0.0033` n `6`; index avg `-0.1185` n `25`; metal avg `-0.1091` n `20`; unknown avg `-0.0268` n `793`
- 1h: commodity avg `-0.0753` n `12`; crypto_alt avg `-1.5928` n `231`; crypto_major avg `-1.4311` n `8`; equity avg `-1.8154` n `122`; fx avg `0.0241` n `6`; index avg `-0.2451` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.5395` n `793`
- 4h: commodity avg `0.1209` n `12`; crypto_alt avg `-0.1538` n `231`; crypto_major avg `0.2646` n `8`; equity avg `-1.8804` n `122`; fx avg `0.0205` n `6`; index avg `-0.2682` n `25`; metal avg `0.1274` n `20`; unknown avg `0.7266` n `793`
- 24h: commodity avg `-0.0763` n `12`; crypto_alt avg `-1.0494` n `231`; crypto_major avg `-0.7266` n `8`; equity avg `-3.2819` n `122`; fx avg `-0.1178` n `6`; index avg `-0.3935` n `25`; metal avg `0.2342` n `20`; unknown avg `3.6904` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
