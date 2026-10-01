# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T10:07:33.344262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `13`; crypto_alt avg `-0.6384` n `234`; crypto_major avg `-0.3148` n `8`; equity avg `-0.1887` n `142`; fx avg `-0.0255` n `6`; index avg `-0.0404` n `26`; metal avg `-0.0592` n `20`; unknown avg `0.1786` n `973`
- 1h: commodity avg `-0.0521` n `13`; crypto_alt avg `-0.8143` n `234`; crypto_major avg `-0.2661` n `8`; equity avg `-0.1287` n `142`; fx avg `-0.0164` n `6`; index avg `-0.0294` n `26`; metal avg `-0.0177` n `20`; unknown avg `1.2622` n `973`
- 4h: commodity avg `0.3749` n `13`; crypto_alt avg `-1.719` n `234`; crypto_major avg `-1.1201` n `8`; equity avg `-0.9485` n `142`; fx avg `-0.0396` n `6`; index avg `-0.2249` n `26`; metal avg `-0.4813` n `20`; unknown avg `8.9453` n `956`
- 24h: commodity avg `-0.025` n `13`; crypto_alt avg `-1.095` n `234`; crypto_major avg `-0.2371` n `8`; equity avg `0.2192` n `142`; fx avg `0.0489` n `6`; index avg `0.0934` n `26`; metal avg `-0.3858` n `20`; unknown avg `776.8417` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
