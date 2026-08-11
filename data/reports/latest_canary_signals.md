# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T23:07:25.033792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0641` n `230`; crypto_major avg `-0.0734` n `8`; equity avg `0.1606` n `113`; fx avg `-0.0015` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0335` n `786`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.1643` n `230`; crypto_major avg `-0.2692` n `8`; equity avg `0.2727` n `113`; fx avg `-0.001` n `6`; index avg `0.0058` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0845` n `786`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `0.4618` n `230`; crypto_major avg `0.8803` n `8`; equity avg `0.9507` n `113`; fx avg `-0.0025` n `6`; index avg `0.0559` n `25`; metal avg `0.0674` n `20`; unknown avg `0.5584` n `785`
- 24h: commodity avg `0.1753` n `12`; crypto_alt avg `-1.1119` n `230`; crypto_major avg `0.5783` n `8`; equity avg `1.5933` n `113`; fx avg `-0.0716` n `6`; index avg `0.1211` n `25`; metal avg `-0.2491` n `20`; unknown avg `-0.0792` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
