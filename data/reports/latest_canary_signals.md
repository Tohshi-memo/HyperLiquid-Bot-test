# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T00:27:35.625949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `-0.0627` n `239`; crypto_major avg `-0.0373` n `8`; equity avg `-0.1637` n `166`; fx avg `-0.0118` n `6`; index avg `-0.0216` n `27`; metal avg `-0.0094` n `20`; unknown avg `0.3835` n `1259`
- 1h: commodity avg `0.022` n `13`; crypto_alt avg `0.0911` n `239`; crypto_major avg `0.0428` n `8`; equity avg `0.2859` n `166`; fx avg `-0.0484` n `6`; index avg `0.111` n `27`; metal avg `-0.1127` n `20`; unknown avg `319.1461` n `1252`
- 4h: commodity avg `-0.3878` n `13`; crypto_alt avg `0.0263` n `239`; crypto_major avg `0.5012` n `8`; equity avg `0.5334` n `166`; fx avg `0.0669` n `6`; index avg `0.1009` n `27`; metal avg `0.2521` n `20`; unknown avg `166.4799` n `1202`
- 24h: commodity avg `-0.4801` n `13`; crypto_alt avg `0.535` n `239`; crypto_major avg `0.8515` n `8`; equity avg `1.2195` n `166`; fx avg `0.0635` n `6`; index avg `0.1572` n `27`; metal avg `0.2818` n `20`; unknown avg `242.7896` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
