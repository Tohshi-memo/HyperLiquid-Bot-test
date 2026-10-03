# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T01:37:30.088385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0975` n `13`; crypto_alt avg `-0.088` n `235`; crypto_major avg `0.0382` n `8`; equity avg `0.0082` n `143`; fx avg `0.0036` n `6`; index avg `0.0038` n `26`; metal avg `0.0047` n `20`; unknown avg `0.0189` n `984`
- 1h: commodity avg `-0.1991` n `13`; crypto_alt avg `-0.1165` n `235`; crypto_major avg `-0.0201` n `8`; equity avg `-0.0206` n `143`; fx avg `0.0087` n `6`; index avg `0.0106` n `26`; metal avg `-0.0216` n `20`; unknown avg `0.0037` n `982`
- 4h: commodity avg `-0.1802` n `13`; crypto_alt avg `1.6122` n `235`; crypto_major avg `1.0901` n `8`; equity avg `0.0731` n `143`; fx avg `0.0065` n `6`; index avg `0.019` n `26`; metal avg `-0.0202` n `20`; unknown avg `1.5608` n `960`
- 24h: commodity avg `0.0523` n `13`; crypto_alt avg `0.0032` n `235`; crypto_major avg `0.1502` n `8`; equity avg `0.9484` n `142`; fx avg `-0.1425` n `6`; index avg `0.338` n `26`; metal avg `-0.0242` n `20`; unknown avg `-0.523` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
