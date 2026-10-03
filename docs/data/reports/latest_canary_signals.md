# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T13:22:26.768816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `-0.1318` n `235`; crypto_major avg `-0.1547` n `8`; equity avg `-0.0087` n `143`; fx avg `-0.0019` n `6`; index avg `-0.0005` n `26`; metal avg `-0.004` n `20`; unknown avg `0.1448` n `984`
- 1h: commodity avg `0.0297` n `13`; crypto_alt avg `-0.0559` n `235`; crypto_major avg `-0.1143` n `8`; equity avg `-0.0168` n `143`; fx avg `-0.0021` n `6`; index avg `0.0005` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.4799` n `982`
- 4h: commodity avg `0.0309` n `13`; crypto_alt avg `0.4679` n `235`; crypto_major avg `0.1109` n `8`; equity avg `0.0121` n `143`; fx avg `-0.0142` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0772` n `972`
- 24h: commodity avg `0.5561` n `13`; crypto_alt avg `-2.6129` n `235`; crypto_major avg `-2.5632` n `8`; equity avg `-0.4194` n `143`; fx avg `0.0368` n `6`; index avg `-0.0534` n `26`; metal avg `-0.2816` n `20`; unknown avg `0.167` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
