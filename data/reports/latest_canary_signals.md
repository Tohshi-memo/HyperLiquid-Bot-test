# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T05:52:31.352668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0542` n `13`; crypto_alt avg `0.0256` n `235`; crypto_major avg `0.0024` n `8`; equity avg `0.0419` n `144`; fx avg `0.006` n `6`; index avg `0.0141` n `26`; metal avg `0.0075` n `20`; unknown avg `-0.5917` n `1079`
- 1h: commodity avg `-0.0593` n `13`; crypto_alt avg `0.3899` n `235`; crypto_major avg `0.1062` n `8`; equity avg `0.0203` n `144`; fx avg `0.0019` n `6`; index avg `0.0048` n `26`; metal avg `0.0352` n `20`; unknown avg `1.2352` n `1077`
- 4h: commodity avg `-0.0423` n `13`; crypto_alt avg `-0.4152` n `235`; crypto_major avg `-0.5986` n `8`; equity avg `-0.421` n `144`; fx avg `-0.021` n `6`; index avg `-0.109` n `26`; metal avg `-0.1746` n `20`; unknown avg `2.9113` n `986`
- 24h: commodity avg `-0.3455` n `13`; crypto_alt avg `0.267` n `235`; crypto_major avg `0.7771` n `8`; equity avg `0.2079` n `144`; fx avg `-0.0492` n `6`; index avg `-0.0578` n `26`; metal avg `0.057` n `20`; unknown avg `0.0376` n `904`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
