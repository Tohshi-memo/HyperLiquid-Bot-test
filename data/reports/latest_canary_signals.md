# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T09:37:29.998896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0646` n `13`; crypto_alt avg `-0.1103` n `235`; crypto_major avg `-0.0769` n `8`; equity avg `-0.1092` n `144`; fx avg `0.0058` n `6`; index avg `-0.0274` n `26`; metal avg `-0.0741` n `20`; unknown avg `0.2267` n `1079`
- 1h: commodity avg `-0.1688` n `13`; crypto_alt avg `-0.2627` n `235`; crypto_major avg `-0.4284` n `8`; equity avg `-0.1359` n `144`; fx avg `0.0043` n `6`; index avg `-0.0241` n `26`; metal avg `-0.0252` n `20`; unknown avg `0.951` n `1077`
- 4h: commodity avg `0.1269` n `13`; crypto_alt avg `0.4776` n `235`; crypto_major avg `0.5172` n `8`; equity avg `-0.0598` n `144`; fx avg `0.0359` n `6`; index avg `-0.0136` n `26`; metal avg `0.2225` n `20`; unknown avg `-0.4403` n `981`
- 24h: commodity avg `-0.1608` n `13`; crypto_alt avg `0.7743` n `235`; crypto_major avg `0.9148` n `8`; equity avg `0.1177` n `144`; fx avg `-0.026` n `6`; index avg `-0.0806` n `26`; metal avg `0.2777` n `20`; unknown avg `-0.1432` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
