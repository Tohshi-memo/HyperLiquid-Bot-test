# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T03:22:25.049028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0423` n `13`; crypto_alt avg `0.0379` n `239`; crypto_major avg `-0.0181` n `8`; equity avg `-0.0434` n `162`; fx avg `0.0066` n `6`; index avg `0.0037` n `27`; metal avg `0.0198` n `20`; unknown avg `-0.0288` n `1263`
- 1h: commodity avg `-0.0586` n `13`; crypto_alt avg `0.0225` n `239`; crypto_major avg `-0.1035` n `8`; equity avg `-0.192` n `162`; fx avg `-0.0044` n `6`; index avg `-0.039` n `27`; metal avg `-0.0595` n `20`; unknown avg `-0.1084` n `1261`
- 4h: commodity avg `-0.0915` n `13`; crypto_alt avg `-0.0697` n `239`; crypto_major avg `-0.3172` n `8`; equity avg `-0.7983` n `162`; fx avg `-0.0188` n `6`; index avg `-0.1612` n `27`; metal avg `-0.3048` n `20`; unknown avg `0.087` n `1241`
- 24h: commodity avg `-0.4404` n `13`; crypto_alt avg `0.0594` n `239`; crypto_major avg `0.0869` n `8`; equity avg `0.3983` n `162`; fx avg `-0.0068` n `6`; index avg `0.0503` n `27`; metal avg `0.1418` n `20`; unknown avg `0.746` n `1125`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
