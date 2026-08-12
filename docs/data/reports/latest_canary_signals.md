# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T19:22:31.113416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.1556` n `230`; crypto_major avg `-0.0766` n `8`; equity avg `-0.0458` n `113`; fx avg `0.0036` n `6`; index avg `-0.01` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.1087` n `786`
- 1h: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.2826` n `230`; crypto_major avg `-0.0747` n `8`; equity avg `-0.1225` n `113`; fx avg `-0.0112` n `6`; index avg `0.002` n `25`; metal avg `0.0282` n `20`; unknown avg `-0.1056` n `786`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.3179` n `230`; crypto_major avg `-0.0014` n `8`; equity avg `0.3698` n `113`; fx avg `-0.0014` n `6`; index avg `0.025` n `25`; metal avg `-0.1421` n `20`; unknown avg `0.1375` n `786`
- 24h: commodity avg `0.01` n `12`; crypto_alt avg `-0.4738` n `230`; crypto_major avg `0.742` n `8`; equity avg `3.7124` n `113`; fx avg `0.0233` n `6`; index avg `0.4425` n `25`; metal avg `0.2902` n `20`; unknown avg `0.159` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
