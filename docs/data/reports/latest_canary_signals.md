# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T18:22:35.566310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0639` n `230`; crypto_major avg `-0.0964` n `8`; equity avg `0.0344` n `113`; fx avg `0.0101` n `6`; index avg `0.009` n `25`; metal avg `0.0419` n `20`; unknown avg `-0.0713` n `786`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `0.0499` n `230`; crypto_major avg `0.0748` n `8`; equity avg `0.2918` n `113`; fx avg `0.0014` n `6`; index avg `0.0166` n `25`; metal avg `0.007` n `20`; unknown avg `0.7554` n `786`
- 4h: commodity avg `0.0778` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `0.1155` n `8`; equity avg `0.7273` n `113`; fx avg `0.0048` n `6`; index avg `0.0209` n `25`; metal avg `-0.2356` n `20`; unknown avg `0.2063` n `786`
- 24h: commodity avg `0.0964` n `12`; crypto_alt avg `-0.1867` n `230`; crypto_major avg `0.6651` n `8`; equity avg `3.9924` n `113`; fx avg `0.0429` n `6`; index avg `0.4439` n `25`; metal avg `0.2912` n `20`; unknown avg `0.1502` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2272`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
