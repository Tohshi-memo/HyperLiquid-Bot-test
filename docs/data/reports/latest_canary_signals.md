# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T17:22:30.149595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.1189` n `230`; crypto_major avg `-0.1458` n `8`; equity avg `-0.02` n `113`; fx avg `0.0114` n `6`; index avg `-0.0107` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.1054` n `786`
- 1h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.0918` n `230`; crypto_major avg `-0.1103` n `8`; equity avg `-0.011` n `113`; fx avg `0.0099` n `6`; index avg `0.0102` n `25`; metal avg `-0.1164` n `20`; unknown avg `-0.058` n `786`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `-0.6292` n `230`; crypto_major avg `-0.6517` n `8`; equity avg `0.3635` n `113`; fx avg `0.0206` n `6`; index avg `-0.0436` n `25`; metal avg `-0.2119` n `20`; unknown avg `0.1081` n `786`
- 24h: commodity avg `0.014` n `12`; crypto_alt avg `-0.2136` n `230`; crypto_major avg `0.81` n `8`; equity avg `3.7013` n `113`; fx avg `0.055` n `6`; index avg `0.4207` n `25`; metal avg `0.1854` n `20`; unknown avg `0.0514` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
