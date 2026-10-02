# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T08:45:26.540923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0287` n `13`; crypto_alt avg `-0.0671` n `234`; crypto_major avg `-0.1315` n `8`; equity avg `-0.0548` n `142`; fx avg `-0.006` n `6`; index avg `-0.0073` n `26`; metal avg `-0.052` n `20`; unknown avg `0.0024` n `985`
- 1h: commodity avg `-0.3641` n `13`; crypto_alt avg `0.5391` n `234`; crypto_major avg `0.6295` n `8`; equity avg `0.306` n `142`; fx avg `-0.0319` n `6`; index avg `0.0517` n `26`; metal avg `-0.009` n `20`; unknown avg `-0.4179` n `907`
- 4h: commodity avg `-0.6167` n `13`; crypto_alt avg `0.3215` n `234`; crypto_major avg `0.0526` n `8`; equity avg `0.4185` n `142`; fx avg `-0.1339` n `6`; index avg `0.1067` n `26`; metal avg `0.0236` n `20`; unknown avg `0.1125` n `891`
- 24h: commodity avg `-0.7751` n `13`; crypto_alt avg `1.8067` n `234`; crypto_major avg `2.4737` n `8`; equity avg `1.3815` n `142`; fx avg `-0.322` n `6`; index avg `0.2888` n `26`; metal avg `0.2978` n `20`; unknown avg `0.6838` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
