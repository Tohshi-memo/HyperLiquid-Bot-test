# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:52:24.283843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.082` n `231`; crypto_major avg `-0.1354` n `8`; equity avg `-0.0535` n `122`; fx avg `-0.0054` n `6`; index avg `-0.0113` n `25`; metal avg `0.0385` n `20`; unknown avg `-0.0599` n `794`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `0.0077` n `231`; crypto_major avg `0.2976` n `8`; equity avg `-0.1137` n `122`; fx avg `0.0039` n `6`; index avg `-0.0284` n `25`; metal avg `0.1142` n `20`; unknown avg `-0.045` n `794`
- 4h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.3301` n `231`; crypto_major avg `0.8546` n `8`; equity avg `-0.0711` n `122`; fx avg `-0.0071` n `6`; index avg `-0.0243` n `25`; metal avg `0.2148` n `20`; unknown avg `-0.2957` n `794`
- 24h: commodity avg `-0.0839` n `12`; crypto_alt avg `-1.5919` n `231`; crypto_major avg `-0.6748` n `8`; equity avg `-3.0855` n `122`; fx avg `-0.0687` n `6`; index avg `-0.3927` n `25`; metal avg `0.2937` n `20`; unknown avg `0.7675` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
