# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T08:37:30.225033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1669` n `12`; crypto_alt avg `0.1442` n `231`; crypto_major avg `0.0317` n `8`; equity avg `0.1149` n `122`; fx avg `0.0037` n `6`; index avg `0.0217` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0179` n `797`
- 1h: commodity avg `-0.0986` n `12`; crypto_alt avg `0.2013` n `231`; crypto_major avg `-0.0374` n `8`; equity avg `0.1149` n `122`; fx avg `-0.0135` n `6`; index avg `0.017` n `25`; metal avg `-0.05` n `20`; unknown avg `0.0148` n `797`
- 4h: commodity avg `-0.1094` n `12`; crypto_alt avg `-0.0976` n `231`; crypto_major avg `-0.1076` n `8`; equity avg `-0.366` n `122`; fx avg `-0.0106` n `6`; index avg `-0.0576` n `25`; metal avg `-0.1114` n `20`; unknown avg `0.0182` n `781`
- 24h: commodity avg `-0.637` n `12`; crypto_alt avg `-1.8974` n `231`; crypto_major avg `-2.0624` n `8`; equity avg `0.4863` n `122`; fx avg `-0.0361` n `6`; index avg `0.0475` n `25`; metal avg `0.1945` n `20`; unknown avg `0.7944` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
