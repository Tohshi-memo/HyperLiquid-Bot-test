# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T02:37:27.716715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3288` n `232`; crypto_major avg `0.1394` n `8`; equity avg `0.0005` n `132`; fx avg `-0.0122` n `6`; index avg `-0.0122` n `26`; metal avg `0.0632` n `20`; unknown avg `0.1646` n `792`
- 1h: commodity avg `-0.1645` n `12`; crypto_alt avg `0.7526` n `232`; crypto_major avg `0.3082` n `8`; equity avg `-0.043` n `132`; fx avg `0.0035` n `6`; index avg `-0.0109` n `26`; metal avg `0.0573` n `20`; unknown avg `2.645` n `790`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `0.4585` n `232`; crypto_major avg `0.1477` n `8`; equity avg `-0.1313` n `132`; fx avg `-0.0848` n `6`; index avg `-0.0176` n `26`; metal avg `-0.1373` n `20`; unknown avg `-0.0167` n `790`
- 24h: commodity avg `0.8594` n `12`; crypto_alt avg `-0.4345` n `232`; crypto_major avg `-1.6191` n `8`; equity avg `-2.156` n `130`; fx avg `-0.054` n `6`; index avg `-0.3758` n `26`; metal avg `-0.9516` n `20`; unknown avg `-0.012` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0412`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0397`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0346`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0296`, n `668`, weak_sample_signal
