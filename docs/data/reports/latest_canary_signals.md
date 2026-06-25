# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T13:22:31.917727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.0505` n `228`; crypto_major avg `-0.0758` n `8`; equity avg `0.0477` n `86`; fx avg `-0.0033` n `6`; index avg `-0.0096` n `23`; metal avg `-0.1113` n `20`; unknown avg `-0.0646` n `765`
- 1h: commodity avg `0.0956` n `12`; crypto_alt avg `0.3898` n `228`; crypto_major avg `0.4217` n `8`; equity avg `0.1594` n `86`; fx avg `0.0305` n `6`; index avg `0.0387` n `23`; metal avg `0.4383` n `20`; unknown avg `0.0995` n `765`
- 4h: commodity avg `0.1335` n `12`; crypto_alt avg `-0.2647` n `228`; crypto_major avg `-0.6191` n `8`; equity avg `0.1791` n `86`; fx avg `-0.0235` n `6`; index avg `0.0604` n `23`; metal avg `0.4391` n `20`; unknown avg `0.0584` n `765`
- 24h: commodity avg `0.2991` n `12`; crypto_alt avg `-0.1983` n `228`; crypto_major avg `-0.1284` n `8`; equity avg `0.7423` n `86`; fx avg `0.031` n `6`; index avg `0.5662` n `23`; metal avg `0.4067` n `20`; unknown avg `-0.4068` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
