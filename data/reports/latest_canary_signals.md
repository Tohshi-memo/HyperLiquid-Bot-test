# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T15:22:36.862414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0427` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8504` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3873` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0338` n `13`; crypto_alt avg `-0.401` n `236`; crypto_major avg `-0.3541` n `8`; equity avg `-0.2779` n `151`; fx avg `-0.0196` n `6`; index avg `-0.078` n `26`; metal avg `-0.0822` n `20`; unknown avg `-0.2681` n `1152`
- 1h: commodity avg `0.0505` n `13`; crypto_alt avg `-1.5133` n `236`; crypto_major avg `-1.5461` n `8`; equity avg `-1.0405` n `151`; fx avg `-0.0294` n `6`; index avg `-0.1588` n `26`; metal avg `-0.1244` n `20`; unknown avg `4.7027` n `1064`
- 4h: commodity avg `-0.3751` n `13`; crypto_alt avg `-1.9719` n `236`; crypto_major avg `-2.176` n `8`; equity avg `-2.3553` n `151`; fx avg `0.0036` n `6`; index avg `-0.3256` n `26`; metal avg `-0.1333` n `20`; unknown avg `4.6263` n `998`
- 24h: commodity avg `-0.4948` n `13`; crypto_alt avg `-0.0598` n `236`; crypto_major avg `-0.8687` n `8`; equity avg `-1.4848` n `151`; fx avg `0.0361` n `6`; index avg `-0.2581` n `26`; metal avg `0.111` n `20`; unknown avg `14.6696` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1044`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1021`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.084`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.083`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
