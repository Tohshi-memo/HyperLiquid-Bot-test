# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T06:07:27.549343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `12`; crypto_alt avg `0.0776` n `230`; crypto_major avg `0.0951` n `8`; equity avg `0.0248` n `98`; fx avg `-0.0177` n `6`; index avg `0.0007` n `25`; metal avg `0.0514` n `20`; unknown avg `-0.1277` n `753`
- 1h: commodity avg `0.1055` n `12`; crypto_alt avg `-0.342` n `230`; crypto_major avg `-0.277` n `8`; equity avg `-0.2674` n `98`; fx avg `-0.0246` n `6`; index avg `-0.0583` n `25`; metal avg `-0.0969` n `20`; unknown avg `-0.12` n `753`
- 4h: commodity avg `0.0469` n `12`; crypto_alt avg `-1.0484` n `230`; crypto_major avg `-0.9201` n `8`; equity avg `-0.2996` n `98`; fx avg `-0.036` n `6`; index avg `-0.0883` n `25`; metal avg `-0.0462` n `20`; unknown avg `-0.1715` n `753`
- 24h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.7485` n `230`; crypto_major avg `-0.5428` n `8`; equity avg `-0.0367` n `97`; fx avg `-0.0517` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0327` n `20`; unknown avg `-0.0981` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0967`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0895`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
