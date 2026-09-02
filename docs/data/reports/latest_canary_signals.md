# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T15:16:15.506945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.1589` n `232`; crypto_major avg `-0.13` n `8`; equity avg `0.0962` n `133`; fx avg `-0.0154` n `6`; index avg `0.0145` n `26`; metal avg `-0.0392` n `20`; unknown avg `0.4751` n `791`
- 1h: commodity avg `0.2106` n `12`; crypto_alt avg `-0.8257` n `232`; crypto_major avg `-0.8269` n `8`; equity avg `-0.3243` n `133`; fx avg `-0.0223` n `6`; index avg `-0.0151` n `26`; metal avg `-0.1094` n `20`; unknown avg `-0.0921` n `789`
- 4h: commodity avg `0.3028` n `12`; crypto_alt avg `0.0465` n `232`; crypto_major avg `0.4536` n `8`; equity avg `0.7678` n `133`; fx avg `-0.121` n `6`; index avg `0.1916` n `26`; metal avg `0.3949` n `20`; unknown avg `0.2191` n `789`
- 24h: commodity avg `0.6856` n `12`; crypto_alt avg `-1.5029` n `232`; crypto_major avg `-1.8045` n `8`; equity avg `-0.4146` n `132`; fx avg `-0.3573` n `6`; index avg `-0.0535` n `26`; metal avg `0.1107` n `20`; unknown avg `-0.0377` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
