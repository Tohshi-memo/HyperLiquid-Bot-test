# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T04:07:26.237381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0414` n `230`; crypto_major avg `0.0085` n `8`; equity avg `0.048` n `113`; fx avg `-0.007` n `6`; index avg `0.008` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.0902` n `786`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `-0.2054` n `230`; crypto_major avg `0.017` n `8`; equity avg `0.0843` n `113`; fx avg `-0.0228` n `6`; index avg `0.0009` n `25`; metal avg `-0.0971` n `20`; unknown avg `0.1057` n `786`
- 4h: commodity avg `0.1445` n `12`; crypto_alt avg `0.3229` n `230`; crypto_major avg `0.1367` n `8`; equity avg `0.8312` n `113`; fx avg `0.0334` n `6`; index avg `0.1677` n `25`; metal avg `0.1817` n `20`; unknown avg `-0.1545` n `786`
- 24h: commodity avg `0.3629` n `12`; crypto_alt avg `-1.0378` n `230`; crypto_major avg `0.582` n `8`; equity avg `1.6989` n `113`; fx avg `0.0095` n `6`; index avg `0.1289` n `25`; metal avg `-0.1559` n `20`; unknown avg `-0.0657` n `753`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2244`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
