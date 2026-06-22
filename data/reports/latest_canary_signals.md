# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T05:37:26.525413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `-0.0716` n `228`; crypto_major avg `-0.0308` n `8`; equity avg `-0.0593` n `79`; fx avg `0.0026` n `6`; index avg `0.0013` n `23`; metal avg `0.2021` n `18`; unknown avg `-0.1963` n `701`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `0.255` n `228`; crypto_major avg `0.3866` n `8`; equity avg `0.155` n `79`; fx avg `-0.0059` n `6`; index avg `0.0611` n `23`; metal avg `0.3193` n `18`; unknown avg `-0.3911` n `701`
- 4h: commodity avg `-0.1138` n `12`; crypto_alt avg `-0.4618` n `228`; crypto_major avg `-0.5653` n `8`; equity avg `-0.0206` n `79`; fx avg `-0.0013` n `6`; index avg `-0.0632` n `23`; metal avg `-0.0006` n `18`; unknown avg `-0.6231` n `693`
- 24h: commodity avg `-0.3708` n `12`; crypto_alt avg `0.1939` n `228`; crypto_major avg `-0.4628` n `8`; equity avg `-0.5739` n `79`; fx avg `-0.0018` n `6`; index avg `-0.0151` n `23`; metal avg `0.4044` n `18`; unknown avg `-0.4484` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
