# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T02:52:31.309708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.0168` n `233`; crypto_major avg `-0.036` n `8`; equity avg `-0.0103` n `136`; fx avg `0.0086` n `6`; index avg `0.0007` n `27`; metal avg `0.0321` n `20`; unknown avg `-0.0094` n `908`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.1418` n `233`; crypto_major avg `-0.1106` n `8`; equity avg `0.1916` n `136`; fx avg `0.0496` n `6`; index avg `0.0279` n `27`; metal avg `0.1563` n `20`; unknown avg `0.2579` n `906`
- 4h: commodity avg `0.132` n `12`; crypto_alt avg `-0.3699` n `233`; crypto_major avg `-0.47` n `8`; equity avg `0.33` n `136`; fx avg `0.1139` n `6`; index avg `0.1074` n `27`; metal avg `0.0987` n `20`; unknown avg `0.3683` n `900`
- 24h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.4714` n `233`; crypto_major avg `0.6954` n `8`; equity avg `-0.0674` n `136`; fx avg `0.0981` n `6`; index avg `-0.0337` n `27`; metal avg `-0.2598` n `20`; unknown avg `5.2861` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
