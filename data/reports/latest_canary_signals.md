# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T11:52:27.012007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0912` n `12`; crypto_alt avg `0.1166` n `229`; crypto_major avg `0.2235` n `8`; equity avg `0.069` n `91`; fx avg `0.005` n `6`; index avg `0.001` n `25`; metal avg `0.0766` n `20`; unknown avg `0.0867` n `763`
- 1h: commodity avg `-0.1523` n `12`; crypto_alt avg `0.178` n `229`; crypto_major avg `0.2446` n `8`; equity avg `-0.0733` n `91`; fx avg `0.0096` n `6`; index avg `-0.0058` n `25`; metal avg `0.178` n `20`; unknown avg `0.0651` n `763`
- 4h: commodity avg `-0.1757` n `12`; crypto_alt avg `0.346` n `229`; crypto_major avg `0.2183` n `8`; equity avg `-0.3308` n `91`; fx avg `-0.0693` n `6`; index avg `-0.0786` n `25`; metal avg `0.3287` n `20`; unknown avg `-0.1903` n `757`
- 24h: commodity avg `0.2292` n `12`; crypto_alt avg `0.564` n `229`; crypto_major avg `-0.2438` n `8`; equity avg `-1.681` n `90`; fx avg `-0.1404` n `6`; index avg `-0.4467` n `25`; metal avg `-0.0919` n `20`; unknown avg `-0.3183` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
