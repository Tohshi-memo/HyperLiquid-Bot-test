# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T11:52:28.667550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.33` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1513` n `234`; crypto_major avg `0.1053` n `8`; equity avg `-0.0055` n `140`; fx avg `-0.0124` n `6`; index avg `0.0003` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.7047` n `942`
- 1h: commodity avg `-0.0014` n `12`; crypto_alt avg `0.3905` n `234`; crypto_major avg `0.3502` n `8`; equity avg `0.0081` n `140`; fx avg `-0.0224` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.8729` n `940`
- 4h: commodity avg `-0.0244` n `12`; crypto_alt avg `1.6808` n `234`; crypto_major avg `0.5707` n `8`; equity avg `0.0156` n `140`; fx avg `-0.0005` n `6`; index avg `0.0036` n `26`; metal avg `0.0172` n `20`; unknown avg `0.8652` n `934`
- 24h: commodity avg `0.1811` n `12`; crypto_alt avg `4.3808` n `234`; crypto_major avg `3.9989` n `8`; equity avg `0.5125` n `140`; fx avg `-0.0045` n `6`; index avg `0.0105` n `26`; metal avg `-0.1594` n `20`; unknown avg `2.6593` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
