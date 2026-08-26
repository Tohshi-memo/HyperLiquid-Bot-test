# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T13:42:27.736922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1175` n `12`; crypto_alt avg `0.0599` n `231`; crypto_major avg `0.3649` n `8`; equity avg `0.5941` n `122`; fx avg `0.0037` n `6`; index avg `0.078` n `25`; metal avg `0.0231` n `20`; unknown avg `0.1198` n `797`
- 1h: commodity avg `0.2046` n `12`; crypto_alt avg `-0.5216` n `231`; crypto_major avg `-0.1562` n `8`; equity avg `0.4262` n `122`; fx avg `0.0146` n `6`; index avg `0.0621` n `25`; metal avg `-0.0721` n `20`; unknown avg `0.1171` n `797`
- 4h: commodity avg `0.2681` n `12`; crypto_alt avg `-0.0744` n `231`; crypto_major avg `0.0132` n `8`; equity avg `0.1282` n `122`; fx avg `-0.0004` n `6`; index avg `0.0382` n `25`; metal avg `-0.082` n `20`; unknown avg `0.0094` n `797`
- 24h: commodity avg `0.0971` n `12`; crypto_alt avg `-1.4801` n `231`; crypto_major avg `-1.1958` n `8`; equity avg `0.1139` n `122`; fx avg `-0.0579` n `6`; index avg `-0.0029` n `25`; metal avg `0.1874` n `20`; unknown avg `0.6287` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
