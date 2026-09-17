# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T05:42:33.131578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `0.0177` n `234`; crypto_major avg `-0.1238` n `8`; equity avg `-0.1583` n `137`; fx avg `0.0133` n `6`; index avg `-0.0298` n `27`; metal avg `0.0269` n `20`; unknown avg `0.5405` n `921`
- 1h: commodity avg `-0.0701` n `12`; crypto_alt avg `0.3495` n `234`; crypto_major avg `0.0694` n `8`; equity avg `-0.1793` n `137`; fx avg `0.0287` n `6`; index avg `-0.0582` n `27`; metal avg `-0.0174` n `20`; unknown avg `5.777` n `919`
- 4h: commodity avg `-0.0329` n `12`; crypto_alt avg `0.2475` n `234`; crypto_major avg `-0.3806` n `8`; equity avg `-0.1955` n `137`; fx avg `0.0512` n `6`; index avg `-0.0786` n `27`; metal avg `-0.0859` n `20`; unknown avg `0.7434` n `911`
- 24h: commodity avg `-0.4407` n `12`; crypto_alt avg `2.337` n `234`; crypto_major avg `1.0632` n `8`; equity avg `0.963` n `137`; fx avg `0.0308` n `6`; index avg `0.0501` n `27`; metal avg `-0.241` n `20`; unknown avg `0.3204` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
