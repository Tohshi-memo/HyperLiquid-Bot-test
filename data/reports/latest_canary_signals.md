# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T07:13:01.897577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.4355` n `235`; crypto_major avg `0.3033` n `8`; equity avg `0.0809` n `144`; fx avg `-0.002` n `6`; index avg `0.034` n `26`; metal avg `0.0606` n `20`; unknown avg `-0.2708` n `1077`
- 1h: commodity avg `0.0905` n `13`; crypto_alt avg `0.5952` n `235`; crypto_major avg `0.5097` n `8`; equity avg `0.0452` n `144`; fx avg `0.007` n `6`; index avg `0.0239` n `26`; metal avg `0.0845` n `20`; unknown avg `-0.2552` n `1077`
- 4h: commodity avg `0.0462` n `13`; crypto_alt avg `0.2741` n `235`; crypto_major avg `0.1527` n `8`; equity avg `0.0076` n `144`; fx avg `0.0228` n `6`; index avg `0.0064` n `26`; metal avg `0.1694` n `20`; unknown avg `-0.0382` n `970`
- 24h: commodity avg `-0.2831` n `13`; crypto_alt avg `0.9524` n `235`; crypto_major avg `1.4305` n `8`; equity avg `0.3119` n `144`; fx avg `-0.079` n `6`; index avg `-0.0213` n `26`; metal avg `0.2107` n `20`; unknown avg `-0.0722` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
