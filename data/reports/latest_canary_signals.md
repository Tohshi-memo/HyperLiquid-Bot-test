# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T09:22:35.237243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0638` n `13`; crypto_alt avg `-0.1144` n `235`; crypto_major avg `-0.2146` n `8`; equity avg `-0.001` n `144`; fx avg `0.0133` n `6`; index avg `0.0021` n `26`; metal avg `0.0061` n `20`; unknown avg `1.0306` n `1079`
- 1h: commodity avg `0.2669` n `13`; crypto_alt avg `-0.4135` n `235`; crypto_major avg `-0.4074` n `8`; equity avg `-0.2026` n `144`; fx avg `0.0368` n `6`; index avg `-0.0473` n `26`; metal avg `-0.0041` n `20`; unknown avg `1.6991` n `1077`
- 4h: commodity avg `0.2537` n `13`; crypto_alt avg `0.8752` n `235`; crypto_major avg `0.8337` n `8`; equity avg `0.0253` n `144`; fx avg `0.0252` n `6`; index avg `0.0087` n `26`; metal avg `0.2786` n `20`; unknown avg `0.1268` n `981`
- 24h: commodity avg `-0.1012` n `13`; crypto_alt avg `0.6759` n `235`; crypto_major avg `0.9773` n `8`; equity avg `0.2259` n `144`; fx avg `-0.0298` n `6`; index avg `-0.053` n `26`; metal avg `0.3471` n `20`; unknown avg `0.181` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2097`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
