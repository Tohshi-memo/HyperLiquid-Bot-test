# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T18:37:26.894813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.1356` n `235`; crypto_major avg `0.0891` n `8`; equity avg `-0.0068` n `144`; fx avg `0.0034` n `6`; index avg `0.0005` n `26`; metal avg `0.0017` n `20`; unknown avg `1.1326` n `1078`
- 1h: commodity avg `0.0381` n `13`; crypto_alt avg `0.2701` n `235`; crypto_major avg `0.0795` n `8`; equity avg `0.0063` n `144`; fx avg `-0.0174` n `6`; index avg `0.0066` n `26`; metal avg `0.0073` n `20`; unknown avg `0.4502` n `1074`
- 4h: commodity avg `0.0173` n `13`; crypto_alt avg `0.0047` n `235`; crypto_major avg `0.4212` n `8`; equity avg `0.0298` n `144`; fx avg `-0.0006` n `6`; index avg `-0.012` n `26`; metal avg `0.0016` n `20`; unknown avg `0.231` n `1068`
- 24h: commodity avg `0.0263` n `13`; crypto_alt avg `1.0884` n `235`; crypto_major avg `0.8933` n `8`; equity avg `0.2011` n `144`; fx avg `0.0262` n `6`; index avg `-0.0177` n `26`; metal avg `0.0069` n `20`; unknown avg `0.1268` n `1017`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
