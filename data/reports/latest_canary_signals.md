# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T15:37:35.961367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0944` n `13`; crypto_alt avg `-0.0539` n `235`; crypto_major avg `-0.1456` n `8`; equity avg `0.0662` n `144`; fx avg `0.0035` n `6`; index avg `0.016` n `26`; metal avg `0.0963` n `20`; unknown avg `-0.0523` n `1079`
- 1h: commodity avg `0.1041` n `13`; crypto_alt avg `0.0025` n `235`; crypto_major avg `-0.2524` n `8`; equity avg `0.1874` n `144`; fx avg `0.042` n `6`; index avg `0.0169` n `26`; metal avg `0.0776` n `20`; unknown avg `-0.1694` n `1045`
- 4h: commodity avg `0.0382` n `13`; crypto_alt avg `-1.0353` n `235`; crypto_major avg `-0.8545` n `8`; equity avg `0.0969` n `144`; fx avg `-0.0367` n `6`; index avg `0.0821` n `26`; metal avg `-0.122` n `20`; unknown avg `0.5766` n `989`
- 24h: commodity avg `-0.1269` n `13`; crypto_alt avg `0.0031` n `235`; crypto_major avg `0.1985` n `8`; equity avg `0.2068` n `144`; fx avg `-0.1086` n `6`; index avg `0.068` n `26`; metal avg `0.205` n `20`; unknown avg `-0.2934` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
