# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T12:37:30.790218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0409` n `12`; crypto_alt avg `-0.1036` n `231`; crypto_major avg `-0.4154` n `8`; equity avg `-0.277` n `122`; fx avg `-0.012` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.0364` n `797`
- 1h: commodity avg `-0.0725` n `12`; crypto_alt avg `0.1135` n `231`; crypto_major avg `-0.2126` n `8`; equity avg `-0.3625` n `122`; fx avg `-0.0181` n `6`; index avg `-0.0372` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0855` n `797`
- 4h: commodity avg `0.156` n `12`; crypto_alt avg `-0.3472` n `231`; crypto_major avg `-0.4912` n `8`; equity avg `-0.3789` n `122`; fx avg `-0.0208` n `6`; index avg `-0.0349` n `25`; metal avg `-0.0486` n `20`; unknown avg `-0.1252` n `797`
- 24h: commodity avg `-0.1096` n `12`; crypto_alt avg `-0.9277` n `231`; crypto_major avg `-0.9143` n `8`; equity avg `0.0497` n `122`; fx avg `-0.0283` n `6`; index avg `-0.046` n `25`; metal avg `0.1841` n `20`; unknown avg `0.5847` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
