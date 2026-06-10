# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T14:07:35.406417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.277` n `12`; crypto_alt avg `-0.1217` n `228`; crypto_major avg `0.0046` n `8`; equity avg `-0.0381` n `74`; fx avg `-0.0233` n `6`; index avg `0.0398` n `23`; metal avg `-0.1684` n `18`; unknown avg `0.0751` n `547`
- 1h: commodity avg `0.1958` n `12`; crypto_alt avg `1.0564` n `228`; crypto_major avg `1.3023` n `8`; equity avg `1.69` n `74`; fx avg `0.0322` n `6`; index avg `0.5081` n `23`; metal avg `0.6147` n `18`; unknown avg `1.49` n `547`
- 4h: commodity avg `1.1738` n `12`; crypto_alt avg `1.6086` n `228`; crypto_major avg `1.9911` n `8`; equity avg `2.1666` n `74`; fx avg `-0.0175` n `6`; index avg `0.7913` n `23`; metal avg `1.1583` n `18`; unknown avg `1.6519` n `547`
- 24h: commodity avg `1.037` n `12`; crypto_alt avg `0.0782` n `228`; crypto_major avg `-0.8998` n `8`; equity avg `-1.5547` n `74`; fx avg `-0.0542` n `6`; index avg `-1.2196` n `23`; metal avg `-2.2601` n `18`; unknown avg `1.6847` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
