# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T16:37:26.291961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.554` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0524` n `12`; crypto_alt avg `0.0461` n `230`; crypto_major avg `0.1021` n `8`; equity avg `0.0633` n `92`; fx avg `0.0106` n `6`; index avg `0.0556` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0786` n `766`
- 1h: commodity avg `-0.054` n `12`; crypto_alt avg `-0.2112` n `230`; crypto_major avg `-0.0938` n `8`; equity avg `-0.083` n `92`; fx avg `0.001` n `6`; index avg `-0.0124` n `25`; metal avg `-0.1396` n `20`; unknown avg `-0.1345` n `766`
- 4h: commodity avg `-0.1868` n `12`; crypto_alt avg `0.857` n `230`; crypto_major avg `1.4997` n `8`; equity avg `-0.0543` n `92`; fx avg `-0.0175` n `6`; index avg `0.0815` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0606` n `758`
- 24h: commodity avg `0.7317` n `12`; crypto_alt avg `1.7358` n `230`; crypto_major avg `3.4635` n `8`; equity avg `1.1355` n `92`; fx avg `0.0047` n `6`; index avg `0.3634` n `25`; metal avg `0.6377` n `20`; unknown avg `-0.0726` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
