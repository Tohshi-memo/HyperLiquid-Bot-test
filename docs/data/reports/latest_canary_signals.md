# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T18:22:25.210678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0586` n `13`; crypto_alt avg `-0.1822` n `235`; crypto_major avg `-0.1167` n `8`; equity avg `-0.0123` n `143`; fx avg `-0.0022` n `6`; index avg `0.0047` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0007` n `1078`
- 1h: commodity avg `-0.072` n `13`; crypto_alt avg `-0.3851` n `235`; crypto_major avg `-0.0856` n `8`; equity avg `0.017` n `143`; fx avg `-0.0102` n `6`; index avg `0.0055` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.4558` n `1076`
- 4h: commodity avg `-0.0169` n `13`; crypto_alt avg `0.4339` n `235`; crypto_major avg `0.4911` n `8`; equity avg `0.0865` n `143`; fx avg `-0.0084` n `6`; index avg `0.0251` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.2068` n `966`
- 24h: commodity avg `0.1299` n `13`; crypto_alt avg `0.9032` n `235`; crypto_major avg `0.4654` n `8`; equity avg `0.2559` n `143`; fx avg `-0.0552` n `6`; index avg `0.0748` n `26`; metal avg `0.0855` n `20`; unknown avg `-0.1038` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
