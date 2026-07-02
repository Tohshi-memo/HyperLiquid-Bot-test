# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T08:37:30.332378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0354` n `12`; crypto_alt avg `0.073` n `228`; crypto_major avg `0.0778` n `8`; equity avg `0.1982` n `88`; fx avg `-0.0004` n `6`; index avg `0.0516` n `25`; metal avg `0.0262` n `20`; unknown avg `1.6209` n `763`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `0.4323` n `228`; crypto_major avg `0.4029` n `8`; equity avg `0.4287` n `88`; fx avg `-0.0183` n `6`; index avg `0.0738` n `25`; metal avg `0.1567` n `20`; unknown avg `2.1541` n `763`
- 4h: commodity avg `-0.0352` n `12`; crypto_alt avg `0.0076` n `228`; crypto_major avg `-0.2504` n `8`; equity avg `-0.5838` n `88`; fx avg `-0.0612` n `6`; index avg `-0.1172` n `25`; metal avg `0.0755` n `20`; unknown avg `2.7916` n `741`
- 24h: commodity avg `-0.3643` n `12`; crypto_alt avg `2.5689` n `228`; crypto_major avg `2.1236` n `8`; equity avg `-1.8765` n `88`; fx avg `-0.063` n `6`; index avg `-0.5043` n `25`; metal avg `1.2277` n `20`; unknown avg `17.71` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
