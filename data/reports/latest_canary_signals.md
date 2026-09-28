# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T12:22:30.333230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `0.183` n `234`; crypto_major avg `-0.0757` n `8`; equity avg `-0.0374` n `141`; fx avg `0.0132` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0112` n `20`; unknown avg `954.1709` n `962`
- 1h: commodity avg `-0.0863` n `12`; crypto_alt avg `1.1673` n `234`; crypto_major avg `0.6751` n `8`; equity avg `0.2561` n `141`; fx avg `-0.0103` n `6`; index avg `0.0607` n `26`; metal avg `0.1059` n `20`; unknown avg `494.8236` n `954`
- 4h: commodity avg `0.0337` n `12`; crypto_alt avg `1.1961` n `234`; crypto_major avg `1.0364` n `8`; equity avg `0.2794` n `141`; fx avg `0.0167` n `6`; index avg `0.0568` n `26`; metal avg `0.147` n `20`; unknown avg `252.3266` n `952`
- 24h: commodity avg `-0.1956` n `12`; crypto_alt avg `-2.7781` n `234`; crypto_major avg `-2.2546` n `8`; equity avg `-2.4293` n `141`; fx avg `0.0029` n `6`; index avg `-0.1894` n `26`; metal avg `-0.7959` n `20`; unknown avg `4.0739` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
