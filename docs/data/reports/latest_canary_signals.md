# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T15:50:19.310805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.0471` n `230`; crypto_major avg `-0.0201` n `8`; equity avg `0.1495` n `96`; fx avg `-0.0036` n `6`; index avg `0.0231` n `25`; metal avg `0.026` n `20`; unknown avg `-0.0349` n `769`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `0.0928` n `230`; crypto_major avg `0.1036` n `8`; equity avg `0.1191` n `96`; fx avg `0.0593` n `6`; index avg `0.0986` n `25`; metal avg `0.1545` n `20`; unknown avg `-0.0964` n `769`
- 4h: commodity avg `0.1897` n `12`; crypto_alt avg `-0.0896` n `230`; crypto_major avg `-0.2758` n `8`; equity avg `0.7231` n `96`; fx avg `0.073` n `6`; index avg `0.1571` n `25`; metal avg `0.2143` n `20`; unknown avg `-0.0433` n `769`
- 24h: commodity avg `0.4446` n `12`; crypto_alt avg `-2.1182` n `230`; crypto_major avg `-3.0301` n `8`; equity avg `-2.3603` n `94`; fx avg `0.0535` n `6`; index avg `-0.4357` n `25`; metal avg `-0.3677` n `20`; unknown avg `-0.3814` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
