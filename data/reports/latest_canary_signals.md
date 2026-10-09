# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T09:52:29.749928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `0.0689` n `235`; crypto_major avg `-0.0152` n `8`; equity avg `-0.0166` n `150`; fx avg `-0.0021` n `6`; index avg `-0.007` n `26`; metal avg `0.019` n `20`; unknown avg `-0.0372` n `1078`
- 1h: commodity avg `0.0579` n `13`; crypto_alt avg `-0.2063` n `235`; crypto_major avg `-0.03` n `8`; equity avg `-0.1488` n `150`; fx avg `-0.0183` n `6`; index avg `-0.029` n `26`; metal avg `0.0017` n `20`; unknown avg `0.187` n `1076`
- 4h: commodity avg `-0.048` n `13`; crypto_alt avg `0.2478` n `235`; crypto_major avg `0.2146` n `8`; equity avg `0.1896` n `150`; fx avg `-0.0222` n `6`; index avg `0.0398` n `26`; metal avg `-0.006` n `20`; unknown avg `0.4993` n `988`
- 24h: commodity avg `-0.4391` n `13`; crypto_alt avg `-1.9021` n `235`; crypto_major avg `-2.1142` n `8`; equity avg `-0.5318` n `150`; fx avg `0.0835` n `6`; index avg `0.0519` n `26`; metal avg `0.4727` n `20`; unknown avg `7.4047` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
