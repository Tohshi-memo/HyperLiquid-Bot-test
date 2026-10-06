# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T17:22:38.266540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.1292` n `235`; crypto_major avg `-0.1819` n `8`; equity avg `-0.0983` n `150`; fx avg `-0.0094` n `6`; index avg `-0.025` n `26`; metal avg `-0.0305` n `20`; unknown avg `-0.2644` n `1076`
- 1h: commodity avg `0.0971` n `13`; crypto_alt avg `-0.4363` n `235`; crypto_major avg `-0.3538` n `8`; equity avg `-0.1178` n `150`; fx avg `0.0014` n `6`; index avg `-0.0543` n `26`; metal avg `-0.0248` n `20`; unknown avg `0.4184` n `1074`
- 4h: commodity avg `0.3321` n `13`; crypto_alt avg `-0.749` n `235`; crypto_major avg `-0.6573` n `8`; equity avg `-0.0296` n `150`; fx avg `0.0041` n `6`; index avg `-0.0837` n `26`; metal avg `0.0138` n `20`; unknown avg `5.5716` n `1018`
- 24h: commodity avg `-0.0726` n `13`; crypto_alt avg `-0.0196` n `235`; crypto_major avg `-0.1992` n `8`; equity avg `0.5864` n `149`; fx avg `0.1107` n `6`; index avg `0.0359` n `26`; metal avg `0.042` n `20`; unknown avg `381.8614` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
