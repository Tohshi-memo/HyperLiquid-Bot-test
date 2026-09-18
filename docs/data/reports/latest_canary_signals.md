# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T10:52:30.403033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.1606` n `234`; crypto_major avg `0.0177` n `8`; equity avg `-0.0671` n `140`; fx avg `-0.0085` n `6`; index avg `-0.0147` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.0459` n `927`
- 1h: commodity avg `-0.0485` n `12`; crypto_alt avg `0.2469` n `234`; crypto_major avg `0.4599` n `8`; equity avg `0.103` n `140`; fx avg `-0.0448` n `6`; index avg `0.016` n `26`; metal avg `0.0224` n `20`; unknown avg `-0.4119` n `923`
- 4h: commodity avg `0.0854` n `12`; crypto_alt avg `1.1815` n `234`; crypto_major avg `1.2889` n `8`; equity avg `-0.0512` n `140`; fx avg `0.1002` n `6`; index avg `-0.0288` n `26`; metal avg `0.017` n `20`; unknown avg `1.0885` n `917`
- 24h: commodity avg `-0.1107` n `12`; crypto_alt avg `6.1664` n `234`; crypto_major avg `5.1611` n `8`; equity avg `1.7052` n `140`; fx avg `0.1784` n `6`; index avg `0.2259` n `26`; metal avg `0.5973` n `20`; unknown avg `2.531` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
