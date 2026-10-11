# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T02:52:25.216296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `13`; crypto_alt avg `-0.1717` n `235`; crypto_major avg `-0.0695` n `8`; equity avg `-0.003` n `150`; fx avg `0.0018` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.0236` n `1117`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `-0.1813` n `235`; crypto_major avg `-0.0038` n `8`; equity avg `0.0007` n `150`; fx avg `0.0027` n `6`; index avg `0.0034` n `26`; metal avg `0.0039` n `20`; unknown avg `-0.2902` n `1115`
- 4h: commodity avg `0.0526` n `13`; crypto_alt avg `0.1636` n `235`; crypto_major avg `-0.0397` n `8`; equity avg `-0.0201` n `150`; fx avg `0.0074` n `6`; index avg `-0.0005` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.0642` n `1109`
- 24h: commodity avg `0.1428` n `13`; crypto_alt avg `1.2206` n `235`; crypto_major avg `0.3223` n `8`; equity avg `0.0882` n `150`; fx avg `-0.005` n `6`; index avg `-0.0109` n `26`; metal avg `0.0032` n `20`; unknown avg `0.3677` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
