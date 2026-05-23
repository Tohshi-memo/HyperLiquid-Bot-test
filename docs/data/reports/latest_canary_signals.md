# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T18:48:21.209069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0965` n `12`; crypto_alt avg `-0.1103` n `228`; crypto_major avg `-0.0531` n `8`; equity avg `-0.066` n `67`; fx avg `0.0006` n `6`; index avg `-0.1242` n `23`; metal avg `0.0009` n `18`; unknown avg `0.0484` n `396`
- 1h: commodity avg `-0.6674` n `12`; crypto_alt avg `1.0116` n `228`; crypto_major avg `0.7887` n `8`; equity avg `0.5285` n `67`; fx avg `0.0004` n `6`; index avg `0.3294` n `23`; metal avg `0.0916` n `18`; unknown avg `1.147` n `396`
- 4h: commodity avg `-0.4829` n `12`; crypto_alt avg `1.9746` n `228`; crypto_major avg `1.3391` n `8`; equity avg `0.6514` n `67`; fx avg `0.005` n `6`; index avg `0.174` n `23`; metal avg `0.2299` n `18`; unknown avg `0.9704` n `396`
- 24h: commodity avg `-0.2902` n `12`; crypto_alt avg `-0.1053` n `228`; crypto_major avg `-0.1884` n `8`; equity avg `-0.0443` n `67`; fx avg `0.0097` n `6`; index avg `0.0544` n `23`; metal avg `-0.0609` n `18`; unknown avg `-1.2033` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
