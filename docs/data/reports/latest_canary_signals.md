# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T07:07:24.491172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `13`; crypto_alt avg `0.0967` n `235`; crypto_major avg `0.02` n `8`; equity avg `0.0062` n `143`; fx avg `0.0011` n `6`; index avg `0.0006` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0259` n `1077`
- 1h: commodity avg `-0.0041` n `13`; crypto_alt avg `0.1358` n `235`; crypto_major avg `0.1512` n `8`; equity avg `-0.0073` n `143`; fx avg `0.0021` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.0896` n `1077`
- 4h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.793` n `235`; crypto_major avg `0.3868` n `8`; equity avg `0.0407` n `143`; fx avg `-0.0185` n `6`; index avg `0.0008` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.2759` n `1043`
- 24h: commodity avg `0.1574` n `13`; crypto_alt avg `2.157` n `235`; crypto_major avg `1.0838` n `8`; equity avg `0.2523` n `143`; fx avg `-0.0438` n `6`; index avg `0.0211` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.4417` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
