# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T07:07:27.009872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `13`; crypto_alt avg `-0.1064` n `235`; crypto_major avg `-0.0281` n `8`; equity avg `-0.1116` n `149`; fx avg `0.0057` n `6`; index avg `-0.0306` n `26`; metal avg `-0.0335` n `20`; unknown avg `0.0609` n `1016`
- 1h: commodity avg `-0.2193` n `13`; crypto_alt avg `0.3186` n `235`; crypto_major avg `0.1789` n `8`; equity avg `-0.0269` n `149`; fx avg `0.0235` n `6`; index avg `-0.0151` n `26`; metal avg `0.0745` n `20`; unknown avg `0.0895` n `1016`
- 4h: commodity avg `-0.2437` n `13`; crypto_alt avg `0.02` n `235`; crypto_major avg `-0.319` n `8`; equity avg `0.0926` n `149`; fx avg `-0.0116` n `6`; index avg `0.0225` n `26`; metal avg `-0.0957` n `20`; unknown avg `-0.031` n `994`
- 24h: commodity avg `-0.3012` n `13`; crypto_alt avg `-1.5613` n `235`; crypto_major avg `-1.0203` n `8`; equity avg `0.1161` n `149`; fx avg `0.0387` n `6`; index avg `0.1072` n `26`; metal avg `-0.1966` n `20`; unknown avg `-0.3704` n `834`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
