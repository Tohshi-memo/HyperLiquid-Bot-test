# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T05:52:32.879888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.1036` n `234`; crypto_major avg `0.0323` n `8`; equity avg `-0.0069` n `142`; fx avg `0.0027` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0345` n `20`; unknown avg `121.9405` n `985`
- 1h: commodity avg `0.0251` n `13`; crypto_alt avg `-0.4901` n `234`; crypto_major avg `-0.6136` n `8`; equity avg `-0.1117` n `142`; fx avg `-0.0315` n `6`; index avg `-0.0157` n `26`; metal avg `0.0243` n `20`; unknown avg `3.7326` n `981`
- 4h: commodity avg `-0.054` n `13`; crypto_alt avg `1.1992` n `234`; crypto_major avg `1.3438` n `8`; equity avg `0.1944` n `142`; fx avg `-0.073` n `6`; index avg `0.0265` n `26`; metal avg `0.3309` n `20`; unknown avg `4.3372` n `975`
- 24h: commodity avg `0.3775` n `13`; crypto_alt avg `0.0323` n `234`; crypto_major avg `0.7782` n `8`; equity avg `0.0192` n `142`; fx avg `-0.2828` n `6`; index avg `-0.0653` n `26`; metal avg `-0.1503` n `20`; unknown avg `0.1679` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
