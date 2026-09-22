# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T07:52:30.319386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `12`; crypto_alt avg `0.2538` n `234`; crypto_major avg `0.1242` n `8`; equity avg `-0.01` n `140`; fx avg `0.0134` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0113` n `20`; unknown avg `1.6744` n `944`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.1579` n `234`; crypto_major avg `-0.4029` n `8`; equity avg `-0.1237` n `140`; fx avg `0.0212` n `6`; index avg `-0.0336` n `26`; metal avg `-0.0554` n `20`; unknown avg `0.5474` n `942`
- 4h: commodity avg `0.0734` n `12`; crypto_alt avg `0.0063` n `234`; crypto_major avg `-0.1271` n `8`; equity avg `-0.9201` n `140`; fx avg `0.038` n `6`; index avg `-0.1371` n `26`; metal avg `-0.2164` n `20`; unknown avg `8.4676` n `908`
- 24h: commodity avg `-0.144` n `12`; crypto_alt avg `2.6038` n `234`; crypto_major avg `3.6516` n `8`; equity avg `1.1407` n `140`; fx avg `-0.1549` n `6`; index avg `0.2606` n `26`; metal avg `-0.2236` n `20`; unknown avg `1125.7381` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
