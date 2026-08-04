# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T19:37:43.938106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.0194` n `230`; crypto_major avg `0.0436` n `8`; equity avg `-0.086` n `107`; fx avg `0.0001` n `6`; index avg `-0.0108` n `25`; metal avg `-0.045` n `20`; unknown avg `-0.0113` n `782`
- 1h: commodity avg `-0.0383` n `12`; crypto_alt avg `0.0946` n `230`; crypto_major avg `0.0118` n `8`; equity avg `0.053` n `107`; fx avg `0.0262` n `6`; index avg `0.027` n `25`; metal avg `-0.0325` n `20`; unknown avg `-0.0929` n `782`
- 4h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.7577` n `230`; crypto_major avg `0.5757` n `8`; equity avg `0.6997` n `107`; fx avg `0.0792` n `6`; index avg `0.2232` n `25`; metal avg `0.0534` n `20`; unknown avg `-0.0726` n `782`
- 24h: commodity avg `-1.2057` n `12`; crypto_alt avg `-0.1078` n `230`; crypto_major avg `0.435` n `8`; equity avg `3.9601` n `107`; fx avg `0.1571` n `6`; index avg `0.8538` n `25`; metal avg `0.9277` n `20`; unknown avg `0.5112` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
