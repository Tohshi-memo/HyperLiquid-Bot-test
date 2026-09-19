# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T07:52:32.883926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `0.0836` n `234`; crypto_major avg `-0.0189` n `8`; equity avg `0.0192` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0047` n `20`; unknown avg `1.3333` n `942`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `-0.0619` n `234`; crypto_major avg `-0.1576` n `8`; equity avg `0.0317` n `140`; fx avg `0.0098` n `6`; index avg `0.0239` n `26`; metal avg `0.0043` n `20`; unknown avg `0.8421` n `940`
- 4h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.9801` n `234`; crypto_major avg `-0.4757` n `8`; equity avg `-0.0749` n `140`; fx avg `-0.007` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0119` n `20`; unknown avg `43.5567` n `896`
- 24h: commodity avg `0.317` n `12`; crypto_alt avg `2.7294` n `234`; crypto_major avg `3.7362` n `8`; equity avg `0.0749` n `140`; fx avg `0.0146` n `6`; index avg `-0.0943` n `26`; metal avg `-0.2665` n `20`; unknown avg `2.0126` n `803`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
