# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T05:26:21.762115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `0.1178` n `231`; crypto_major avg `0.0803` n `8`; equity avg `0.233` n `122`; fx avg `0.0174` n `6`; index avg `0.0282` n `25`; metal avg `0.055` n `20`; unknown avg `-0.1593` n `794`
- 1h: commodity avg `-0.0822` n `12`; crypto_alt avg `0.4449` n `231`; crypto_major avg `0.3367` n `8`; equity avg `0.3695` n `122`; fx avg `-0.0164` n `6`; index avg `0.0368` n `25`; metal avg `0.0833` n `20`; unknown avg `0.2608` n `794`
- 4h: commodity avg `-0.084` n `12`; crypto_alt avg `1.1376` n `231`; crypto_major avg `1.0067` n `8`; equity avg `1.2737` n `122`; fx avg `0.01` n `6`; index avg `0.2082` n `25`; metal avg `-0.2957` n `20`; unknown avg `1.029` n `794`
- 24h: commodity avg `-0.0658` n `12`; crypto_alt avg `1.9735` n `231`; crypto_major avg `2.957` n `8`; equity avg `0.0258` n `122`; fx avg `0.0362` n `6`; index avg `-0.0473` n `25`; metal avg `-0.0726` n `20`; unknown avg `0.6447` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
