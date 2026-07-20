# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T04:37:30.698747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.2624` n `230`; crypto_major avg `0.3211` n `8`; equity avg `0.2873` n `98`; fx avg `-0.0021` n `6`; index avg `0.0926` n `25`; metal avg `0.0299` n `20`; unknown avg `2.3432` n `769`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1654` n `230`; crypto_major avg `-0.0608` n `8`; equity avg `0.2767` n `98`; fx avg `-0.0071` n `6`; index avg `0.0618` n `25`; metal avg `-0.0352` n `20`; unknown avg `0.0369` n `769`
- 4h: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.5626` n `230`; crypto_major avg `-0.3212` n `8`; equity avg `-0.4559` n `98`; fx avg `-0.0484` n `6`; index avg `-0.0905` n `25`; metal avg `0.1288` n `20`; unknown avg `-0.17` n `769`
- 24h: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.0922` n `230`; crypto_major avg `0.0903` n `8`; equity avg `0.416` n `97`; fx avg `-0.0045` n `6`; index avg `0.0927` n `25`; metal avg `0.1041` n `20`; unknown avg `0.0744` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
