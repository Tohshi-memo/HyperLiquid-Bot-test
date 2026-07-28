# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T22:52:25.744733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.24` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `-0.3196` n `230`; crypto_major avg `-0.2967` n `8`; equity avg `-0.8364` n `102`; fx avg `-0.0016` n `6`; index avg `-0.1136` n `25`; metal avg `0.0079` n `20`; unknown avg `0.0662` n `776`
- 1h: commodity avg `0.4079` n `12`; crypto_alt avg `-0.5802` n `230`; crypto_major avg `-0.6329` n `8`; equity avg `-1.0602` n `102`; fx avg `-0.0098` n `6`; index avg `-0.1664` n `25`; metal avg `-0.1069` n `20`; unknown avg `0.2221` n `776`
- 4h: commodity avg `0.6874` n `12`; crypto_alt avg `-0.144` n `230`; crypto_major avg `0.0348` n `8`; equity avg `-0.1018` n `102`; fx avg `-0.0201` n `6`; index avg `-0.1111` n `25`; metal avg `-0.0785` n `20`; unknown avg `0.2716` n `775`
- 24h: commodity avg `-0.2501` n `12`; crypto_alt avg `-0.7568` n `230`; crypto_major avg `-0.4732` n `8`; equity avg `-3.2683` n `102`; fx avg `-0.0817` n `6`; index avg `-0.4741` n `25`; metal avg `-0.4809` n `20`; unknown avg `0.2335` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
