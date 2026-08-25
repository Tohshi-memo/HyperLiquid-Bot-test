# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T00:07:26.140075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.2952` n `231`; crypto_major avg `0.3185` n `8`; equity avg `-0.131` n `122`; fx avg `-0.0107` n `6`; index avg `-0.0567` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0606` n `794`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `0.4975` n `231`; crypto_major avg `0.6489` n `8`; equity avg `-0.2835` n `122`; fx avg `-0.0095` n `6`; index avg `-0.084` n `25`; metal avg `0.0762` n `20`; unknown avg `-0.0034` n `794`
- 4h: commodity avg `0.0315` n `12`; crypto_alt avg `0.5243` n `231`; crypto_major avg `1.0027` n `8`; equity avg `-0.2369` n `122`; fx avg `-0.0154` n `6`; index avg `-0.0817` n `25`; metal avg `0.2174` n `20`; unknown avg `-0.2757` n `794`
- 24h: commodity avg `-0.0929` n `12`; crypto_alt avg `-0.6801` n `231`; crypto_major avg `-0.0402` n `8`; equity avg `-3.0232` n `122`; fx avg `-0.0483` n `6`; index avg `-0.4255` n `25`; metal avg `0.1732` n `20`; unknown avg `0.8654` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
