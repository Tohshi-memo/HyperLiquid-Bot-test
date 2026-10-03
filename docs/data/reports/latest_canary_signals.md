# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T09:37:28.050288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `13`; crypto_alt avg `-0.0509` n `235`; crypto_major avg `-0.0308` n `8`; equity avg `0.0023` n `143`; fx avg `-0.0003` n `6`; index avg `0.0047` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.2045` n `984`
- 1h: commodity avg `-0.0097` n `13`; crypto_alt avg `-0.0552` n `235`; crypto_major avg `0.045` n `8`; equity avg `0.0078` n `143`; fx avg `-0.009` n `6`; index avg `0.0038` n `26`; metal avg `0.0049` n `20`; unknown avg `1.3077` n `982`
- 4h: commodity avg `0.0604` n `13`; crypto_alt avg `-0.6772` n `235`; crypto_major avg `-0.2412` n `8`; equity avg `0.0023` n `143`; fx avg `-0.003` n `6`; index avg `-0.0129` n `26`; metal avg `0.0022` n `20`; unknown avg `0.2874` n `944`
- 24h: commodity avg `0.7155` n `13`; crypto_alt avg `-2.4592` n `235`; crypto_major avg `-2.2684` n `8`; equity avg `-0.0215` n `142`; fx avg `0.0091` n `6`; index avg `0.1235` n `26`; metal avg `-0.31` n `20`; unknown avg `-0.2137` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1844`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1735`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1089`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `669`, weak_sample_signal
