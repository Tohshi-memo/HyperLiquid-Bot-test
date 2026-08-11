# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T21:22:29.004164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.0738` n `230`; crypto_major avg `0.0047` n `8`; equity avg `-0.0865` n `113`; fx avg `0.0011` n `6`; index avg `-0.0012` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0586` n `785`
- 1h: commodity avg `-0.0775` n `12`; crypto_alt avg `-0.1285` n `230`; crypto_major avg `0.0797` n `8`; equity avg `0.0622` n `113`; fx avg `-0.0024` n `6`; index avg `0.0014` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0342` n `785`
- 4h: commodity avg `-0.086` n `12`; crypto_alt avg `0.2928` n `230`; crypto_major avg `0.8371` n `8`; equity avg `0.6722` n `113`; fx avg `0.0114` n `6`; index avg `0.0534` n `25`; metal avg `-0.037` n `20`; unknown avg `0.4953` n `785`
- 24h: commodity avg `0.0177` n `12`; crypto_alt avg `-1.2087` n `230`; crypto_major avg `0.3926` n `8`; equity avg `1.2098` n `113`; fx avg `-0.0678` n `6`; index avg `0.1183` n `25`; metal avg `-0.2538` n `20`; unknown avg `-0.2928` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2175`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
