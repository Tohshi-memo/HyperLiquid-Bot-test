# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T07:07:30.939282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.099` n `234`; crypto_major avg `-0.1245` n `8`; equity avg `-0.0994` n `140`; fx avg `-0.0149` n `6`; index avg `-0.0132` n `26`; metal avg `0.0063` n `20`; unknown avg `0.0041` n `942`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.3334` n `234`; crypto_major avg `0.2333` n `8`; equity avg `-0.0957` n `140`; fx avg `0.0076` n `6`; index avg `-0.03` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.4263` n `938`
- 4h: commodity avg `0.0504` n `12`; crypto_alt avg `0.395` n `234`; crypto_major avg `0.4096` n `8`; equity avg `-0.9392` n `140`; fx avg `-0.0116` n `6`; index avg `-0.119` n `26`; metal avg `-0.1676` n `20`; unknown avg `0.3967` n `908`
- 24h: commodity avg `-0.1032` n `12`; crypto_alt avg `2.5503` n `234`; crypto_major avg `3.9152` n `8`; equity avg `1.2162` n `140`; fx avg `-0.1899` n `6`; index avg `0.2851` n `26`; metal avg `-0.2129` n `20`; unknown avg `1125.8276` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
