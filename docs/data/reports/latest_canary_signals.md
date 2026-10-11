# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T13:22:27.185115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `13`; crypto_alt avg `0.063` n `235`; crypto_major avg `0.0859` n `8`; equity avg `0.02` n `150`; fx avg `-0.0013` n `6`; index avg `-0.0125` n `26`; metal avg `0.0007` n `20`; unknown avg `0.1571` n `1134`
- 1h: commodity avg `-0.0197` n `13`; crypto_alt avg `0.2081` n `235`; crypto_major avg `-0.0811` n `8`; equity avg `-0.01` n `150`; fx avg `0.0065` n `6`; index avg `-0.0083` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.0917` n `1059`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `0.1103` n `235`; crypto_major avg `0.1022` n `8`; equity avg `0.0946` n `150`; fx avg `0.0254` n `6`; index avg `-0.0047` n `26`; metal avg `0.0034` n `20`; unknown avg `0.6892` n `1053`
- 24h: commodity avg `0.2996` n `13`; crypto_alt avg `1.2083` n `235`; crypto_major avg `-0.0076` n `8`; equity avg `0.1559` n `150`; fx avg `0.0198` n `6`; index avg `0.0019` n `26`; metal avg `0.0125` n `20`; unknown avg `0.6317` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
