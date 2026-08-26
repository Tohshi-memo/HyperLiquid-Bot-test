# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T02:52:26.008438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0583` n `12`; crypto_alt avg `-0.0804` n `231`; crypto_major avg `-0.0553` n `8`; equity avg `0.1577` n `122`; fx avg `0.0098` n `6`; index avg `0.0404` n `25`; metal avg `0.0344` n `20`; unknown avg `0.1789` n `797`
- 1h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.5945` n `231`; crypto_major avg `0.3657` n `8`; equity avg `0.631` n `122`; fx avg `0.0345` n `6`; index avg `0.1446` n `25`; metal avg `0.1074` n `20`; unknown avg `0.5985` n `796`
- 4h: commodity avg `-0.1082` n `12`; crypto_alt avg `0.8484` n `231`; crypto_major avg `0.359` n `8`; equity avg `-0.0929` n `122`; fx avg `0.0066` n `6`; index avg `0.0191` n `25`; metal avg `0.1085` n `20`; unknown avg `0.5215` n `795`
- 24h: commodity avg `-0.9181` n `12`; crypto_alt avg `-2.1875` n `231`; crypto_major avg `-2.3033` n `8`; equity avg `1.8268` n `122`; fx avg `0.0345` n `6`; index avg `0.2863` n `25`; metal avg `0.4106` n `20`; unknown avg `0.1739` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
