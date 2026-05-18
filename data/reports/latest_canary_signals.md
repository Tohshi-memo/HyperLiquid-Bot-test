# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T04:37:14.947728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.0104` n `228`; crypto_major avg `0.0128` n `8`; equity avg `-0.2024` n `66`; fx avg `-0.0063` n `5`; index avg `-0.1092` n `23`; metal avg `-0.0708` n `18`; unknown avg `-0.0692` n `383`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `0.0202` n `228`; crypto_major avg `0.0103` n `8`; equity avg `-0.0011` n `66`; fx avg `0.0129` n `5`; index avg `0.0064` n `23`; metal avg `0.4004` n `18`; unknown avg `-0.2321` n `383`
- 4h: commodity avg `0.3768` n `12`; crypto_alt avg `0.3145` n `228`; crypto_major avg `-0.4387` n `8`; equity avg `0.5755` n `66`; fx avg `0.0691` n `5`; index avg `0.2731` n `23`; metal avg `0.6014` n `18`; unknown avg `-0.5211` n `383`
- 24h: commodity avg `2.7046` n `12`; crypto_alt avg `-10.9472` n `228`; crypto_major avg `-3.4615` n `8`; equity avg `-3.1214` n `65`; fx avg `-0.0669` n `5`; index avg `-1.7776` n `23`; metal avg `-6.096` n `18`; unknown avg `550.0607` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
