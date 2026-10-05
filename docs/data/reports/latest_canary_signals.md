# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T22:07:28.040311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `13`; crypto_alt avg `0.1377` n `235`; crypto_major avg `0.21` n `8`; equity avg `0.0187` n `144`; fx avg `0.0178` n `6`; index avg `-0.0012` n `26`; metal avg `0.0178` n `20`; unknown avg `-0.1152` n `1075`
- 1h: commodity avg `0.0062` n `13`; crypto_alt avg `0.577` n `235`; crypto_major avg `0.415` n `8`; equity avg `0.0613` n `144`; fx avg `0.0074` n `6`; index avg `0.0099` n `26`; metal avg `0.0297` n `20`; unknown avg `0.1514` n `1025`
- 4h: commodity avg `-0.0694` n `13`; crypto_alt avg `1.1872` n `235`; crypto_major avg `0.7671` n `8`; equity avg `0.0841` n `144`; fx avg `0.0075` n `6`; index avg `0.0228` n `26`; metal avg `0.007` n `20`; unknown avg `0.2793` n `979`
- 24h: commodity avg `-0.2969` n `13`; crypto_alt avg `0.9036` n `235`; crypto_major avg `0.2347` n `8`; equity avg `0.3257` n `144`; fx avg `-0.0909` n `6`; index avg `0.1331` n `26`; metal avg `0.1136` n `20`; unknown avg `630.465` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
