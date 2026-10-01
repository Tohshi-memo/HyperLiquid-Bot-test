# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T21:37:32.543049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.2757` n `234`; crypto_major avg `-0.2453` n `8`; equity avg `-0.0242` n `142`; fx avg `0.0099` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.1981` n `985`
- 1h: commodity avg `0.1187` n `13`; crypto_alt avg `-0.6302` n `234`; crypto_major avg `-0.4202` n `8`; equity avg `-0.0761` n `142`; fx avg `0.0247` n `6`; index avg `-0.0134` n `26`; metal avg `0.0373` n `20`; unknown avg `-0.8202` n `981`
- 4h: commodity avg `0.2727` n `13`; crypto_alt avg `-0.5951` n `234`; crypto_major avg `-0.6657` n `8`; equity avg `-0.1963` n `142`; fx avg `0.0771` n `6`; index avg `-0.0096` n `26`; metal avg `0.0092` n `20`; unknown avg `1.4624` n `931`
- 24h: commodity avg `0.1898` n `13`; crypto_alt avg `-0.4605` n `234`; crypto_major avg `-0.5708` n `8`; equity avg `1.1257` n `142`; fx avg `-0.1009` n `6`; index avg `0.2282` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.3241` n `856`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
