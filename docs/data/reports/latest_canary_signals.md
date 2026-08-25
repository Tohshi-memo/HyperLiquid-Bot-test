# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:04:50.087667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `0.3398` n `231`; crypto_major avg `0.4434` n `8`; equity avg `0.1472` n `122`; fx avg `0.0141` n `6`; index avg `0.014` n `25`; metal avg `-0.0111` n `20`; unknown avg `0.0315` n `794`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.3359` n `231`; crypto_major avg `-0.0889` n `8`; equity avg `0.1168` n `122`; fx avg `0.0474` n `6`; index avg `0.048` n `25`; metal avg `0.0085` n `20`; unknown avg `-0.068` n `794`
- 4h: commodity avg `-0.2386` n `12`; crypto_alt avg `-0.2376` n `231`; crypto_major avg `-0.2335` n `8`; equity avg `0.9838` n `122`; fx avg `0.0334` n `6`; index avg `0.1803` n `25`; metal avg `0.0602` n `20`; unknown avg `-0.147` n `778`
- 24h: commodity avg `-0.1559` n `12`; crypto_alt avg `1.7515` n `231`; crypto_major avg `2.4066` n `8`; equity avg `0.3855` n `122`; fx avg `0.0205` n `6`; index avg `0.0801` n `25`; metal avg `-0.1897` n `20`; unknown avg `0.5004` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
