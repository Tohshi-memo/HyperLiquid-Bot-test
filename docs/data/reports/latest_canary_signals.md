# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T01:52:32.441831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.194` n `231`; crypto_major avg `-0.332` n `8`; equity avg `0.0537` n `122`; fx avg `-0.0` n `6`; index avg `0.0177` n `25`; metal avg `-0.0549` n `20`; unknown avg `0.3006` n `794`
- 1h: commodity avg `0.1146` n `12`; crypto_alt avg `-0.3739` n `231`; crypto_major avg `-0.3134` n `8`; equity avg `0.1958` n `122`; fx avg `0.0013` n `6`; index avg `0.0383` n `25`; metal avg `-0.1161` n `20`; unknown avg `0.0153` n `794`
- 4h: commodity avg `0.0761` n `12`; crypto_alt avg `0.4286` n `231`; crypto_major avg `1.1999` n `8`; equity avg `0.1682` n `122`; fx avg `0.0236` n `6`; index avg `0.0038` n `25`; metal avg `0.0604` n `20`; unknown avg `1.072` n `794`
- 24h: commodity avg `0.1342` n `12`; crypto_alt avg `1.0635` n `231`; crypto_major avg `1.7607` n `8`; equity avg `-1.833` n `122`; fx avg `0.0027` n `6`; index avg `-0.2794` n `25`; metal avg `0.2246` n `20`; unknown avg `0.8597` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
