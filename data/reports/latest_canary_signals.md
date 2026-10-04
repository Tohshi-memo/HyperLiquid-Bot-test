# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T20:37:30.505662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `0.0321` n `235`; crypto_major avg `0.1022` n `8`; equity avg `0.0161` n `144`; fx avg `-0.0004` n `6`; index avg `0.001` n `26`; metal avg `0.0044` n `20`; unknown avg `4.4476` n `1078`
- 1h: commodity avg `0.0238` n `13`; crypto_alt avg `-0.0368` n `235`; crypto_major avg `0.0393` n `8`; equity avg `0.047` n `144`; fx avg `0.0007` n `6`; index avg `0.0075` n `26`; metal avg `-0.0018` n `20`; unknown avg `7.307` n `1064`
- 4h: commodity avg `0.0971` n `13`; crypto_alt avg `0.4304` n `235`; crypto_major avg `0.2828` n `8`; equity avg `0.0656` n `144`; fx avg `0.0022` n `6`; index avg `0.0082` n `26`; metal avg `0.0205` n `20`; unknown avg `1.8907` n `1064`
- 24h: commodity avg `0.029` n `13`; crypto_alt avg `0.7502` n `235`; crypto_major avg `1.0282` n `8`; equity avg `0.1931` n `144`; fx avg `0.0193` n `6`; index avg `-0.0105` n `26`; metal avg `0.0072` n `20`; unknown avg `0.4275` n `1020`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
