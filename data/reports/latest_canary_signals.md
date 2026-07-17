# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T06:37:26.427792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `0.065` n `230`; crypto_major avg `0.1591` n `8`; equity avg `0.0002` n `96`; fx avg `0.0152` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0582` n `20`; unknown avg `-0.0034` n `768`
- 1h: commodity avg `-0.1295` n `12`; crypto_alt avg `0.0107` n `230`; crypto_major avg `0.006` n `8`; equity avg `0.3695` n `96`; fx avg `0.0441` n `6`; index avg `0.0678` n `25`; metal avg `0.1069` n `20`; unknown avg `-0.0101` n `736`
- 4h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.0499` n `230`; crypto_major avg `-0.5002` n `8`; equity avg `-0.3259` n `94`; fx avg `0.0348` n `6`; index avg `-0.1051` n `25`; metal avg `0.0764` n `20`; unknown avg `-0.0875` n `736`
- 24h: commodity avg `-0.1855` n `12`; crypto_alt avg `-2.0909` n `230`; crypto_major avg `-3.5389` n `8`; equity avg `-5.5284` n `94`; fx avg `-0.0784` n `6`; index avg `-0.7348` n `25`; metal avg `-0.6638` n `20`; unknown avg `-0.5681` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
