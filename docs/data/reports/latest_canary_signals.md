# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T09:07:35.848495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1412` n `12`; crypto_alt avg `-0.7314` n `234`; crypto_major avg `-0.6242` n `8`; equity avg `-0.0179` n `140`; fx avg `0.0419` n `6`; index avg `-0.0082` n `26`; metal avg `-0.1136` n `20`; unknown avg `0.9927` n `942`
- 1h: commodity avg `-0.2821` n `12`; crypto_alt avg `-0.0357` n `234`; crypto_major avg `0.1828` n `8`; equity avg `0.2642` n `140`; fx avg `-0.1063` n `6`; index avg `0.0463` n `26`; metal avg `0.0975` n `20`; unknown avg `0.4216` n `942`
- 4h: commodity avg `-0.3601` n `12`; crypto_alt avg `0.1999` n `234`; crypto_major avg `0.2558` n `8`; equity avg `-0.3085` n `140`; fx avg `-0.0468` n `6`; index avg `-0.0525` n `26`; metal avg `-0.1598` n `20`; unknown avg `9.1103` n `908`
- 24h: commodity avg `-0.5056` n `12`; crypto_alt avg `1.3166` n `234`; crypto_major avg `1.9126` n `8`; equity avg `0.6316` n `140`; fx avg `-0.2358` n `6`; index avg `0.2142` n `26`; metal avg `-0.2113` n `20`; unknown avg `1120.1862` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
