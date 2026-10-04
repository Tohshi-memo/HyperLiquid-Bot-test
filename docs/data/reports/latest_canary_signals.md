# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T05:07:27.484383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `0.0429` n `235`; crypto_major avg `0.0332` n `8`; equity avg `0.0167` n `143`; fx avg `-0.0001` n `6`; index avg `0.0037` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.0738` n `1077`
- 1h: commodity avg `0.0306` n `13`; crypto_alt avg `0.3766` n `235`; crypto_major avg `0.0535` n `8`; equity avg `0.0371` n `143`; fx avg `-0.0011` n `6`; index avg `0.0023` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.0801` n `1077`
- 4h: commodity avg `-0.0268` n `13`; crypto_alt avg `0.5317` n `235`; crypto_major avg `0.1667` n `8`; equity avg `0.0704` n `143`; fx avg `0.0004` n `6`; index avg `-0.0017` n `26`; metal avg `0.009` n `20`; unknown avg `-0.1271` n `1071`
- 24h: commodity avg `0.189` n `13`; crypto_alt avg `1.7568` n `235`; crypto_major avg `0.8955` n `8`; equity avg `0.2867` n `143`; fx avg `-0.0255` n `6`; index avg `0.0231` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.2344` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
