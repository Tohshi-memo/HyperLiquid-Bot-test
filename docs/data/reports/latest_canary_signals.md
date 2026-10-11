# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T06:07:28.615079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `13`; crypto_alt avg `-0.085` n `235`; crypto_major avg `-0.0823` n `8`; equity avg `-0.0121` n `150`; fx avg `0.0015` n `6`; index avg `0.0016` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.1217` n `1099`
- 1h: commodity avg `-0.022` n `13`; crypto_alt avg `-0.1092` n `235`; crypto_major avg `-0.2165` n `8`; equity avg `-0.0429` n `150`; fx avg `-0.0041` n `6`; index avg `0.0003` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.0216` n `1099`
- 4h: commodity avg `0.0958` n `13`; crypto_alt avg `-0.6734` n `235`; crypto_major avg `-0.4245` n `8`; equity avg `-0.1109` n `150`; fx avg `0.0026` n `6`; index avg `-0.016` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.2121` n `1093`
- 24h: commodity avg `0.1409` n `13`; crypto_alt avg `0.4221` n `235`; crypto_major avg `-0.2598` n `8`; equity avg `-0.0329` n `150`; fx avg `-0.0107` n `6`; index avg `-0.038` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.3545` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
