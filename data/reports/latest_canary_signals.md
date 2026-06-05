# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T11:52:23.669183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.0608` n `228`; crypto_major avg `-0.1113` n `8`; equity avg `-0.0604` n `74`; fx avg `0.0154` n `6`; index avg `-0.0194` n `23`; metal avg `0.1672` n `18`; unknown avg `2.5264` n `424`
- 1h: commodity avg `-0.1964` n `12`; crypto_alt avg `-0.2186` n `228`; crypto_major avg `-0.2072` n `8`; equity avg `-0.2064` n `74`; fx avg `0.0374` n `6`; index avg `-0.0935` n `23`; metal avg `0.105` n `18`; unknown avg `2.015` n `424`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `-0.6199` n `228`; crypto_major avg `-0.5261` n `8`; equity avg `0.3948` n `74`; fx avg `0.0754` n `6`; index avg `0.0383` n `23`; metal avg `0.3592` n `18`; unknown avg `2.3013` n `424`
- 24h: commodity avg `-0.0616` n `12`; crypto_alt avg `-4.1684` n `228`; crypto_major avg `-2.8444` n `8`; equity avg `-0.1699` n `73`; fx avg `0.1303` n `6`; index avg `0.0775` n `23`; metal avg `-0.7266` n `18`; unknown avg `0.1992` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
