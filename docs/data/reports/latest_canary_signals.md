# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T03:37:31.985307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `0.1236` n `230`; crypto_major avg `0.0509` n `8`; equity avg `0.0315` n `96`; fx avg `0.0067` n `6`; index avg `-0.0108` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0966` n `770`
- 1h: commodity avg `0.0564` n `12`; crypto_alt avg `-0.2629` n `230`; crypto_major avg `-0.3756` n `8`; equity avg `-0.0017` n `96`; fx avg `0.0052` n `6`; index avg `0.0191` n `25`; metal avg `0.0212` n `20`; unknown avg `0.8116` n `770`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.0438` n `230`; crypto_major avg `0.134` n `8`; equity avg `0.1709` n `96`; fx avg `0.0552` n `6`; index avg `-0.0005` n `25`; metal avg `0.0686` n `20`; unknown avg `-0.4296` n `770`
- 24h: commodity avg `0.3172` n `12`; crypto_alt avg `-0.1373` n `230`; crypto_major avg `0.7316` n `8`; equity avg `-0.2013` n `96`; fx avg `-0.0145` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.0948` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
