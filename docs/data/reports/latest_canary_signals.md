# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T19:22:42.310248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0363` n `13`; crypto_alt avg `0.3032` n `235`; crypto_major avg `0.2262` n `8`; equity avg `-0.0038` n `150`; fx avg `0.0056` n `6`; index avg `0.0013` n `26`; metal avg `0.0253` n `20`; unknown avg `0.797` n `1077`
- 1h: commodity avg `0.0861` n `13`; crypto_alt avg `0.2732` n `235`; crypto_major avg `0.4333` n `8`; equity avg `-0.1085` n `150`; fx avg `0.0116` n `6`; index avg `-0.017` n `26`; metal avg `-0.065` n `20`; unknown avg `1.6535` n `1075`
- 4h: commodity avg `-0.3627` n `13`; crypto_alt avg `1.1768` n `235`; crypto_major avg `0.3968` n `8`; equity avg `0.1871` n `150`; fx avg `-0.0049` n `6`; index avg `0.0639` n `26`; metal avg `0.0187` n `20`; unknown avg `0.033` n `1068`
- 24h: commodity avg `0.3492` n `13`; crypto_alt avg `-4.1933` n `235`; crypto_major avg `-3.045` n `8`; equity avg `-1.4858` n `150`; fx avg `-0.1706` n `6`; index avg `-0.2394` n `26`; metal avg `-0.759` n `20`; unknown avg `15.6528` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
