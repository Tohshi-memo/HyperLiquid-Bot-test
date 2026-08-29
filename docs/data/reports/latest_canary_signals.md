# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T16:52:24.014964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0839` n `231`; crypto_major avg `0.1084` n `8`; equity avg `0.003` n `128`; fx avg `-0.0009` n `6`; index avg `-0.0017` n `26`; metal avg `0.0092` n `20`; unknown avg `0.1393` n `792`
- 1h: commodity avg `0.041` n `12`; crypto_alt avg `0.0726` n `231`; crypto_major avg `0.2412` n `8`; equity avg `0.0257` n `128`; fx avg `-0.0056` n `6`; index avg `0.0031` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.019` n `790`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `0.9288` n `231`; crypto_major avg `1.0053` n `8`; equity avg `0.0519` n `128`; fx avg `-0.0025` n `6`; index avg `0.0065` n `26`; metal avg `0.0588` n `20`; unknown avg `0.3101` n `778`
- 24h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.5393` n `231`; crypto_major avg `0.2606` n `8`; equity avg `-0.0285` n `128`; fx avg `-0.0674` n `6`; index avg `-0.03` n `26`; metal avg `-0.0945` n `20`; unknown avg `0.0031` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2223`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
